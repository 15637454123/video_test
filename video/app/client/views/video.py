# coding:utf-8

from django.views.generic import View
from app.libs.base_render import render_to_response
from app.models import Video
from app.consts import FromType
from django.shortcuts import redirect, reverse, get_object_or_404
from app.utils.permission import client_auth


class ExVideo(View):
    TEMPLATE = 'client/video/video.html'

    def get(self, request):

        data = {}

        videos = Video.objects.exclude(from_to=FromType.custom.value)
        data['videos'] = videos

        return render_to_response(request, self.TEMPLATE, data=data)


class CusVideo(View):
    TEMPLATE = 'client/video/video.html'

    def get(self, request):

        data = {}

        videos = Video.objects.filter(from_to=FromType.custom.value)
        data['videos'] = videos

        return render_to_response(request, self.TEMPLATE, data=data)


class VideoSub(View):
    TEMPLATE = 'client/video/video_sub.html'

    def get(self, request, video_id):
        data = {}

        video = get_object_or_404(Video, pk=video_id)
        data['video'] = video
        user = client_auth(request)
        data['user'] = user
        return render_to_response(request, self.TEMPLATE, data=data)




