# -*- coding: utf-8 -*-
# Create your views here.
#from django.template.loader import get_template  
#from django.template import Template, Context  
#from django.http import Http404, HttpResponse  
from django.shortcuts import render_to_response, render, redirect, reverse
from django.utils import timezone
from board.models import Board
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from board.forms import BoardForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.core.urlresolvers import reverse

# 한글!!
#===========================================================================================
rowsPerPage = 2    
 

def home(request, page=1):
    # if searchStr == None:
    searchStr = request.GET.get('searchStr')
       
    if request.path == '/':
        return redirect('/board/1/')

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
    return render(request, 'lists.html', {'boards': boards, 'page':page, 'searchStr':searchStr})

#===========================================================================================
def write(request, page=1):
    searchStr = request.GET.get('searchStr')
    form = BoardForm(data=request.POST or None)
    if form.is_valid():
        board_ = form.save()
        # return redirect(board_)
        # return redirect('board_view', board_id=board_.id, page=page)
        # return HttpResponseRedirect('board_view', {'board_id':board_.id, 'page':page, 'searchStr':searchStr})
        # return HttpResponseRedirect()
        return redirect(reverse('board_view', args=(board_.id,page))+'?searchStr='+searchStr)
    return render(request, 'writeBoard.html', {"form": form, 'page':page, 'searchStr':searchStr})  

def modify(request, board_id, page):
    searchStr = request.GET.get('searchStr')
    instance = Board.objects.get(id=board_id)
    form = BoardForm(request.POST or None, instance=instance)
    if form.is_valid():
        board_ = form.save()
        return redirect('board_view', board_id=board_.id, page=page)
    return render(request, 'modifyBoard.html', {"form": form, 'page':page, 'searchStr':searchStr})     

def delete(reqeust, board_id, page):
    searchStr = reqeust.GET.get('searchStr')
    board_ = Board.objects.get(id=board_id)
    board_.delete()
    # return redirect('board', page=page, searchStr=searchStr)
    return redirect(reverse('home', args=(page))+'?searchStr='+searchStr)

def view(request, board_id, page):
    searchStr = request.GET.get('searchStr')
    board_ = Board.objects.get(id=board_id)
    board_.hits+=1
    board_.save()
    return render(request, 'viewBoard.html', {'board':board_, 'page':page, 'searchStr':searchStr})

