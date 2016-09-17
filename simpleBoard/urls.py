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
from board import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='no'),
    url(r'^board/(\d+)/', views.home, name='home'),
    url(r'^write/(\d+)/', views.write, name='new_board'),
    url(r'^modify/(\d+)/(\d+)/', views.modify, name='modify'),
    url(r'^view/(\d+)/(\d+)/', views.view, name='board_view'),
    url(r'^delete/(\d+)/(\d+)/', views.delete, name='delete'),
    url(r'^viewWork/$', views.viewWork),       
    url(r'^searchWithSubject/$', views.searchWithSubject),
]
