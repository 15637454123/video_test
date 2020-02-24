# coding:utf-8

from django.urls import path
from .views.base import Index
from .views.auth import Login, AdminManger,Logout


urlpatterns = [
    path('', Index.as_view(), name='dashboard_index'),
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('admin/manager', AdminManger.as_view(), name='admin_manager')
]
