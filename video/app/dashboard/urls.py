# coding:utf-8

from django.urls import path
from .views.base import Index
from .views.auth import Login, AdminManger, Logout, UpdateAdminStatus
from .views.video import ExternaVideo, VideoSubT


urlpatterns = [
    path('', Index.as_view(), name='dashboard_index'),
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('admin/manager', AdminManger.as_view(), name='admin_manager'),
    path('admin/manager/update/status', UpdateAdminStatus.as_view(), name='update_admin_status'),
    path('video/externa', ExternaVideo.as_view(), name='externa_video'),
    path('video/videosub/<int:video_id>', VideoSubT.as_view(), name='video_sub')

]
