from django.shortcuts import render_to_response, render, redirect, reverse
from django.utils import timezone
from board.models import Board
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from board.forms import BoardForm, ReplyForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import hashers
#===========================================================================================
rowsPerPage = 2    
# HELP
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def set_password(raw_password):
    return hashers.make_password(raw_password)
    
def check_password(self, raw_password):
    return hashers.check_password(raw_password)


def board_home(request):
    # if searchStr == None:
    searchStr = request.GET.get('searchStr')
    page = request.GET.get('page')
       
    if request.path == '/':
        return redirect('/board/')

    if searchStr:
        print ("searchStr", searchStr)
        boardList = Board.objects.filter(subject__contains = searchStr).order_by('-id')
    else:
        searchStr = ''
        boardList = Board.objects.order_by('-id')
            
    paginator = Paginator(boardList, rowsPerPage)
    
    try:
        boards = paginator.page(page)
    except PageNotAnInteger:
        boards = paginator.page(1)
    except EmptyPage:
        boards = paginator.page(paginator.num_pages)
    return render(request, 'lists.html', {'user':request.user,'boards': boards, 'searchStr':searchStr})

#===========================================================================================
def board_write(request):
    
    if not request.user.is_authenticated():
        return redirect('board_home')
    page = request.GET.get('page')
    searchStr = request.GET.get('searchStr')
    
    if request.POST:
        print("POST", request.POST.get('id'))
        form = BoardForm(request.POST)
    else:
        print("GET")
        board = Board.objects.get(id=request.GET.get('board_id'))
        form = BoardForm(instance=board)
    
    if form.is_valid():
        board_ = form.save()
        return redirect(reverse('board_view', kwargs={'board_id':board_.id})+'?page='+page+'&searchStr='+searchStr)
    return render(request, 'writeBoard.html', {"form": form, 'page':page, 'searchStr':searchStr})

def board_edit(request, board_id):
    if not request.user.is_authenticated():
        return redirect('board_home')
    page = request.GET.get('page')
    searchStr = request.GET.get('searchStr')
    
    if request.POST:
        board = Board.objects.get(id=board_id)
        form = BoardForm(request.POST, instance=board)
    else:
        print("GET")
        board = Board.objects.get(id=board_id)
        form = BoardForm(instance=board)
    
    if form.is_valid():
        board_ = form.save()
        return redirect(reverse('board_view', kwargs={'board_id':board_.id})+'?page='+page+'&searchStr='+searchStr)
    return render(request, 'editBoard.html', {"form": form, "board_id": board_id, 'page':page, 'searchStr':searchStr})

def board_delete(request, board_id):
    if not request.user.is_authenticated():
        return redirect('board_home')
    page = request.GET.get('page')
    searchStr = request.GET.get('searchStr')
    board_ = Board.objects.get(id=board_id)
    board_.delete()
    # return redirect('board', page=page, searchStr=searchStr)
    return redirect(reverse('board_home')+'?page='+page+'&searchStr='+searchStr)

def board_view(request, board_id):
    page = request.GET.get('page')
    searchStr = request.GET.get('searchStr')
    board_ = Board.objects.get(id=board_id)
    board_.hits+=1
    board_.save()
    reply_form = ReplyForm()
    replys = board_.get_replys()
    return render(request, 'viewBoard.html', {'reply_form':reply_form, 'board':board_, 'page':page, 'searchStr':searchStr, 'replys':replys})


def reply_write(request, board_id):
    page = request.GET.get('page')
    searchStr = request.GET.get('searchStr')
    depth_id = request.GET.get('depthId')
    
    if depth_id is None:
        print ("depth_id=========", depth_id)
        depth_id = 0
    
    ipaddress = get_client_ip(request)
    
    password = set_password(request.POST.get('password'))
    form = ReplyForm(request.POST)
    if form.is_valid():
        board = Board.objects.get(id=board_id)    
        reply = form.save(for_board=board, ipaddress=ipaddress, depth_id=depth_id, password=password)
        print ("reply write!!!")
    return redirect(reverse('board_view', kwargs={'board_id':board_id})+'?page='+page+'&searchStr='+searchStr)

def reply_delete(request, board_id, reply_id):
    page = request.GET.get('page')
    searchStr = request.GET.get('searchStr')
    reply = Reply.objects.get(id=reply_id)
    if reply is not None:
        reply.delete()
    return redirect(reverse('board_view', kwargs={'board_id':board_id})+'?page='+page+'&searchStr='+searchStr)
