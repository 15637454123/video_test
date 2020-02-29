# coding:utf-8
from django.conf import settings
import os
import time
import shutil
# from app.tasks.task import video_task
from app.model.viedo import Video, VideoSub
from app.libs.base_qiniu import video_qiniu


# 设置删除
def remove_path(paths):
    for path in paths:
        if os.path.exists(path):
            os.remove(path)


def handle_video(video_file, video_id, number):

    in_path = os.path.join(settings.BASE_DIR, 'app/dashboard/temp_in')
    out_path = os.path.join(settings.BASE_DIR, 'app/dashboard/temp_out')
    in_name = '{}_{}'.format(int(time.time()), video_file.name)
    in_path_name = '/'.join([in_path, in_name])

    temp_path = video_file.temporary_file_path()
    shutil.copyfile(temp_path, in_path_name)

    out_name = '{}_{}'.format(int(time.time()), video_file.name.split('.')[0])
    out_path_name = '/'.join([out_path, out_name])

    # 利用ffmpeg来对视频进行转码
    command = 'ffmpeg -i {} -c copy {}.mp4'.format(in_path_name, out_path_name)
    os.system(command)
    # video = Video.objects.get(pk=video_id)
    # video_sub = VideoSub.objects.create(
    #     video=video,
    #     url='',
    #     number=number
    # )

    # video_task.delay(command, out_path_name, in_path_name, video_file.name, video_sub.id)

    # 判断地址是否有temp_out文件夹下是否有对应视频存在
    out_video_path = '.'.join([out_path_name, 'mp4'])
    if not os.path.exists(out_video_path):
        remove_path([in_path_name, out_video_path])
        return False

    url = video_qiniu.put(video_file.name, out_video_path)

    # 将视频的地址存入数据库
    if url:
        print(url)
        video = Video.objects.get(pk=video_id)

        try:
            VideoSub.objects.create(
                video=video,
                url=url,
                number=number
            )
            return True
        except:
            return False
        finally:
            remove_path([in_path_name, out_video_path])
        remove_path([in_path_name, out_video_path])
    remove_path([in_path_name, out_video_path])
    return False
