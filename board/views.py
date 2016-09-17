# -*- coding: utf-8 -*-
# Create your views here.
#from django.template.loader import get_template  
#from django.template import Template, Context  
#from django.http import Http404, HttpResponse  
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
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
 

def home(request, p=1):   
    if request.path == '/':
        return redirect('/board/'+str(p))
    boardList = Board.objects.order_by('-id')        
    paginator = Paginator(boardList, 2) # Show 25 contacts per page

    # page = request.GET.get('page')
    try:
        boards = paginator.page(p)
    except PageNotAnInteger:
        boards = paginator.page(1)
    except EmptyPage:
        boards = paginator.page(paginator.num_pages)
    return render(request, 'lists.html', {'boards': boards, 'page':p})

#===========================================================================================
def write(request, p=1):
    form = BoardForm(data=request.POST or None)
    if form.is_valid():
        board_ = form.save()
        return redirect(board_, page=p)
    return render(request, 'writeBoard.html', {"form": form, 'page':p})  

def modify(request, board_id, p=1):
    instance = Board.objects.get(id=board_id)
    form = BoardForm(request.POST or None, instance=instance)
    if form.is_valid():
        board_ = form.save()
        print ("form success", p)
        return redirect(board_, page=p)
    return render(request, 'modifyBoard.html', {"form": form, 'page':p})     

def delete(reqeust, board_id, p=1):
    board_ = Board.objects.get(id=board_id)
    board_.delete()
    return redirect('/board/', page=p)

def view(request, board_id, p=1):
    board_ = Board.objects.get(id=board_id)
        
    return render(request, 'viewBoard.html', {'board':board_, 'page':p})

#===========================================================================================
@csrf_exempt
def DoWriteBoard(request):
    # br = Board (subject = request.POST['subject'],
    #                   name = request.POST['name'],
    #                   mail = request.POST['email'],
    #                   memo = request.POST['memo'],
    #                   created_date = timezone.now(),
    #                   hits = 0
    #                  )
    # br.save()

    form = BoardForm(data=request.POST)
    if form.is_valid():
        # list_ = List.objects.create()
        board = form.save()
        return redirect(board)
    return render(request, 'home.html')

    
    # 다시 조회    
    url = '/listSpecificPageWork?current_page=1' 
    return HttpResponseRedirect(url)    



                   

#===========================================================================================
def viewWork(request):
    pk= request.GET['memo_id']    
    #print 'pk='+ pk
    boardData = Board.objects.get(id=pk)
    #print boardData.memo
    
    # Update DataBase
    print ('boardData.hits', boardData.hits)
    Board.objects.filter(id=pk).update(hits = boardData.hits + 1)
      
    return render_to_response('viewMemo.html', {'memo_id': request.GET['memo_id'], 
                                                'current_page':request.GET['current_page'], 
                                                'searchStr': request.GET['searchStr'], 
                                                'boardData': boardData } )            
   
#===========================================================================================
def listSpecificPageWork(request):    
    current_page = request.GET['current_page']
    totalCnt = Board.objects.all().count()                  
    
    print ('current_page=', current_page)
        
    # 페이지를 가지고 범위 데이터를 조회한다 => raw SQL 사용함
    boardList = Board.objects.raw('SELECT Z.* FROM(SELECT X.*, ceil( rownum / %s ) as page FROM ( SELECT ID,SUBJECT,NAME, CREATED_DATE, MAIL,MEMO,HITS \
                                        FROM BOARD_Board  ORDER BY ID DESC ) X ) Z WHERE page = %s', [rowsPerPage, current_page])
    # boardList = Board.objects.    
    print  ('boardList=',boardList, 'count()=', totalCnt)
    
    # 전체 페이지를 구해서 전달...
    pagingHelperIns = pagingHelper();
    
    totalPageList = pagingHelperIns.getTotalPageList( totalCnt, rowsPerPage)
        
    print ('totalPageList', totalPageList)
    
    return render_to_response('listSpecificPage.html', {'boardList': boardList, 'totalCnt': totalCnt, 
                                                        'current_page':int(current_page) ,'totalPageList':totalPageList} )

#===========================================================================================

def listSpecificPageWork_to_update(request):
    memo_id = request.GET['memo_id']
    current_page = request.GET['current_page']
    searchStr = request.GET['searchStr']
    
    #totalCnt = Board.objects.all().count()
    print ('memo_id', memo_id)
    print ('current_page', current_page)
    print ('searchStr', searchStr)
    
    boardData = Board.objects.get(id=memo_id)
      
    return render_to_response('viewForUpdate.html', {'memo_id': request.GET['memo_id'], 
                                                'current_page':request.GET['current_page'], 
                                                'searchStr': request.GET['searchStr'], 
                                                'boardData': boardData } )    

#===========================================================================================
@csrf_exempt
def updateBoard(request):
    memo_id = request.POST['memo_id']
    current_page = request.POST['current_page']
    searchStr = request.POST['searchStr']        
        
    print ('#### updateBoard ######')
    print ('memo_id', memo_id)
    print ('current_page', current_page)
    print ('searchStr', searchStr)
    
    # Update DataBase
    Board.objects.filter(id=memo_id).update(
                                                  mail= request.POST['mail'],
                                                  subject= request.POST['subject'],
                                                  memo= request.POST['memo']
                                                  )
    
    # Display Page => POST 요청은 redirection!
    url = '/listSpecificPageWork?current_page=' + str(current_page)
    return HttpResponseRedirect(url)    
      

#===========================================================================================
def DeleteSpecificRow(request):
    memo_id = request.GET['memo_id']
    current_page = request.GET['current_page']
    print ('#### DeleteSpecificRow ######')
    print ('memo_id', memo_id)
    print ('current_page', current_page)
    
    p = Board.objects.get(id=memo_id)
    p.delete()
    
    # Display Page    
    # 마지막 메모를 삭제하는 경우, 페이지를 하나 줄임.
    totalCnt = Board.objects.all().count()  
    pagingHelperIns = pagingHelper();
    
    totalPageList = pagingHelperIns.getTotalPageList( totalCnt, rowsPerPage)
    print ('totalPages', totalPageList)
    
    if( int(current_page) in totalPageList):
        print ('current_page No Change')
        current_page=current_page
    else:
        current_page= int(current_page)-1
        print ('current_page--')            
            
    url = '/listSpecificPageWork?current_page=' + str(current_page)
    return HttpResponseRedirect(url)    

#===========================================================================================
@csrf_exempt
def searchWithSubject(request):
    searchStr = request.POST['searchStr']
    print ('searchStr', searchStr)
    
    url = '/listSearchedSpecificPageWork?searchStr=' + searchStr +'&pageForView=1'
    return HttpResponseRedirect(url)    
         
        
#===========================================================================================    
def listSearchedSpecificPageWork(request):
    searchStr = request.GET['searchStr']
    pageForView = request.GET['pageForView']
    print ('listSearchedSpecificPageWork:searchStr', searchStr, 'pageForView=', pageForView)
        
    #boardList = Board.objects.filter(subject__contains=searchStr)
    #print  'boardList=',boardList
    
    totalCnt = Board.objects.filter(subject__contains=searchStr).count()
    print  ('totalCnt=',totalCnt)
    
    pagingHelperIns = pagingHelper();
    totalPageList = pagingHelperIns.getTotalPageList( totalCnt, rowsPerPage)
    
    # like 구문 적용방법 
    boardList = Board.objects.raw("""SELECT Z.* FROM ( SELECT X.*, ceil(rownum / %s) as page \
        FROM ( SELECT ID,SUBJECT,NAME, CREATED_DATE, MAIL,MEMO,HITS FROM BOARD_Board \
        WHERE SUBJECT LIKE '%%'||%s||'%%' ORDER BY ID DESC) X ) Z WHERE page = %s""", [rowsPerPage, searchStr, pageForView])
        
    print ('boardList=',boardList)
    
    return render_to_response('listSearchedSpecificPage.html', {'boardList': boardList, 'totalCnt': totalCnt, 
                                                        'pageForView':int(pageForView) ,'searchStr':searchStr, 'totalPageList':totalPageList} )            
    
#===========================================================================================
  
