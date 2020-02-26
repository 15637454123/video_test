# coding:utf-8

from django.views.generic import View
from django.shortcuts import redirect, reverse
from app.utils.permission import dashboard_auth
from app.libs.base_render import render_to_response
from app.model.viedo import Video, VideoSub
from app.consts import FromType


class ExternaVideo(View):
    TEMPLATE = 'dashboard/video/externa_video.html'

    @dashboard_auth
    def get(self, request):

        error = request.GET.get('error', '')
        data = {'error': error}

        # 展示视频

        videos = Video.objects.exclude(from_to=FromType.custom.value)
        data['videos'] = videos

        return render_to_response(request, self.TEMPLATE, data=data)

    def post(self, request):
        name = request.POST.get('name')
        img = request.POST.get('img')
        video_type = request.POST.get('video_type')
        from_to = request.POST.get('from_to')
        nationality = request.POST.get('nationality')
        info = request.POST.get('info')
        print(name, img, video_type, from_to, nationality, info)
        if not all([name, img, video_type, from_to, nationality, info]):
            return redirect('{}?error={}'.format(reverse('externa_video'), '缺少必要字段'))
        Video.objects.create(
            name=name,
            image=img,
            video_type=video_type,
            from_to=from_to,
            nationality=nationality,
            info=info
        )
        return redirect(reverse('externa_video'))


class VideoSubT(View):
    TEMPLATE = 'dashboard/video/video_sub.html'

    @dashboard_auth
    def get(self, request, video_id):
        data = {}
        video = Video.objects.get(pk=video_id)

        data['video'] = video

        return render_to_response(request, self.TEMPLATE, data=data)

    def post(self, request, video_id):
        url = request.POST.get('url')

        video = Video.objects.get(pk=video_id)
        length = video.video_sub.count()

        VideoSub.objects.create(
            video=video,
            url=url,
            number=length+1
        )
        print(url, video_id)
        return redirect(reverse('video_sub', kwargs={'video_id': video_id}))

