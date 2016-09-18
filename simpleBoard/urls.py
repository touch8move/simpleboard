"""simpleBoard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import RedirectView

from board.views import home, write, modify, view, delete 
from account.views import account_login, account_logout, account_add, account_update, account_delete

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='no'),
    url(r'^board/(?P<page>\d+)/', home, name='home'),
    url(r'^write/(?P<page>\d+)/', write, name='new_board'),
    url(r'^modify/(?P<board_id>\d+)/(?P<page>\d+)/', modify, name='modify'),
    url(r'^view/(?P<board_id>\d+)/(?P<page>\d+)/', view, name='board_view'),
    url(r'^delete/(?P<board_id>\d+)/(?P<page>\d+)/', delete, name='delete'),

    # url(r'^account/', account_main, name='account_main'),
    url(r'^account/login', account_login, name='login'),
    url(r'^account/logout', account_logout, name='logout'),
    url(r'^account/create', account_add, name='account_add'),
    url(r'^account/update', account_update, name='account_update'),
    url(r'^account/delete', account_delete, name='account_delete'),
]
