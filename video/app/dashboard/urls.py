# coding:utf-8

from django.urls import path
from .views.base import Index
from .views.auth import Login, AdminManger, Logout, UpdateAdminStatus
from .views.video import ExternaVideo, VideoSubT, VideoStarView, StarDelete, SubDelete, VideoUpdate, VideoUpdateStatus


urlpatterns = [
    path('', Index.as_view(), name='dashboard_index'),
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('admin/manager', AdminManger.as_view(), name='admin_manager'),
    path('admin/manager/update/status', UpdateAdminStatus.as_view(), name='update_admin_status'),
    path('video/externa', ExternaVideo.as_view(), name='externa_video'),
    path('video/videosub/<int:video_id>', VideoSubT.as_view(), name='video_sub'),
    path('video/star', VideoStarView.as_view(), name='video_star'),
    path('video/star/delete/<int:video_id>/<int:star_id>', StarDelete.as_view(), name='star_delete'),
    path('video/sub/delete/<int:video_id>/<int:sub_id>', SubDelete.as_view(), name='sub_delete'),
    path('video/videoupdate/<int:video_id>', VideoUpdate.as_view(), name='video_update'),
    path('video/statusupdate/<int:video_id>', VideoUpdateStatus.as_view(), name='status_update')
]
