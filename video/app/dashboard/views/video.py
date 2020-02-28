# coding:utf-8

from django.views.generic import View
from django.shortcuts import redirect, reverse
from app.utils.permission import dashboard_auth
from app.libs.base_render import render_to_response
from app.model.viedo import Video, VideoSub, VideoStar
from app.consts import FromType
from app.utils.common import handle_video


class ExternaVideo(View):
    TEMPLATE = 'dashboard/video/externa_video.html'

    @dashboard_auth
    def get(self, request):

        error = request.GET.get('error', '')
        data = {'error': error}

        # 展示视频
        cus_videos = Video.objects.filter(from_to=FromType.custom.value)
        data['cus_videos'] = cus_videos

        ex_videos = Video.objects.exclude(from_to=FromType.custom.value)
        data['ex_videos'] = ex_videos

        return render_to_response(request, self.TEMPLATE, data=data)

    def post(self, request):

        name = request.POST.get('name')
        image = request.POST.get('img')
        video_type = request.POST.get('video_type')
        from_to = request.POST.get('from_to')
        nationality = request.POST.get('nationality')
        info = request.POST.get('info')
        video_id = request.POST.get('video_id')

        print(name, image, video_type, from_to, nationality, info, video_id)

        if video_id:
            reverse_path = reverse('video_update', kwargs={'video_id': video_id})

        else:
            reverse_path = reverse('externa_video')

        if not all([name, image, video_type, from_to, nationality, info]):
            return redirect('{}?error={}'.format(reverse_path, '缺少必要字段'))

        if not video_id:
            try:
                Video.objects.create(
                    name=name,
                    image=image,
                    video_type=video_type,
                    from_to=from_to,
                    nationality=nationality,
                    info=info
                )
            except:
                return redirect('{}?error={}'.format(reverse_path, '创建失败'))
        else:
            try:
                video = Video.objects.get(pk=video_id)
                video.name = name
                video.image = image
                video.video_type = video_type
                video.from_to = from_to
                video.nationality = nationality
                video.info = info
                video.save()
            except:
                return redirect('{}?error={}'.format(reverse_path, '修改失败'))
        return redirect(reverse('externa_video'))


class VideoSubT(View):
    TEMPLATE = 'dashboard/video/video_sub.html'

    @dashboard_auth
    def get(self, request, video_id):
        data = {}
        error = request.GET.get('error', '')
        video = Video.objects.get(pk=video_id)

        data['video'] = video
        data['error'] = error

        return render_to_response(request, self.TEMPLATE, data=data)

    def post(self, request, video_id):

        number = request.POST.get('number')
        videosub_id = request.POST.get('videosub_id')

        video = Video.objects.get(pk=video_id)
        path_format = '{}'.format(reverse('video_sub', kwargs={'video_id': video_id}))

        # 通过枚举类型判断上传的是否是一个文件
        if FromType(video.from_to) == FromType.custom:
            file = request.FILES.get('url')
            handle_video(file, video_id, number)
            return redirect(reverse('video_sub', kwargs={'video_id': video_id}))
        else:
            url = request.POST.get('url')

        if not videosub_id:
            if not all([url, number]):

                return redirect('{}?error={}'.format(path_format, '缺少必要字段'))
            try:
                VideoSub.objects.create(
                    video=video,
                    url=url,
                    number=number
                )
            except:
                return redirect('{}?error={}'.format(path_format, '创建失败'))
            return redirect(reverse('video_sub', kwargs={'video_id': video_id}))

        else:
            video_sub = VideoSub.objects.get(pk=videosub_id)
            video_sub.url = url
            video_sub.number = number
            video_sub.save()
            return redirect(reverse('video_sub', kwargs={'video_id': video_id}))


class VideoStarView(View):
    TEMPLATE = 'dashboard/video/video_sub.html'

    @dashboard_auth
    def get(self, request):
        data = {}
        error = request.GET.get('error', '')

        data['error'] = error

        return render_to_response(request, self.TEMPLATE, data=data)

    def post(self, request):
        name = request.POST.get('name')
        identity = request.POST.get('identity')
        video_id = request.POST.get('video_id')

        path_format = '{}'.format(reverse('video_sub', kwargs={'video_id': video_id}))

        if not all([name, identity, video_id]):
            return redirect('{}?error={}'.format(path_format, '缺少必要字段'))

        video = Video.objects.get(pk=video_id)
        try:
            VideoStar.objects.create(
                video=video,
                name=name,
                identity=identity
            )

        except:

            return redirect('{}?error={}'.format(path_format, '创建失败'))

        return redirect(reverse('video_sub', kwargs={'video_id': video_id}))


class StarDelete(View):

    def get(self, request, star_id, video_id):
        VideoStar.objects.filter(pk=star_id).delete()

        return redirect(reverse('video_sub', kwargs={'video_id': video_id}))


class SubDelete(View):
    def get(self, reuqest, sub_id, video_id):

        VideoSub.objects.filter(pk=sub_id).delete()

        return redirect(reverse('video_sub', kwargs={'video_id': video_id}))


class VideoUpdate(View):
    TEMPLATE = 'dashboard/video/video_update.html'

    @dashboard_auth
    def get(self, request, video_id):

        data = {}
        error = request.GET.get('error', '')
        video = Video.objects.get(pk=video_id)
        data['video'] = video
        data['error'] = error

        return render_to_response(request, self.TEMPLATE, data=data)


class VideoUpdateStatus(View):

    def get(self, request, video_id):

        video = Video.objects.get(pk=video_id)
        video.status = not video.status
        video.save()
        return redirect(reverse('externa_video'))


