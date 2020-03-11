# coding:utf-8

import os
import time
from celery import task
from app.libs.base_qiniu import video_qiniu
from app.model.viedo import VideoSub


def remove_path(paths):
    for path in paths:
        if os.path.exists(path):
            os.remove(path)


@task
def video_task(command, out_path_name, in_path_name, video_file_name, video_sub_id):
    print("-------------------------------------------")
    print(command, out_path_name, in_path_name, video_file_name, video_sub_id)
    print("-------------------------------------------")
    os.system(command)

     # 上传七牛云 并返回视频地址


     # 判断地址是否有temp_out文件夹下是否有对应视频存在
    out_video_path = '.'.join([out_path_name, 'mp4'])

    if not os.path.exists(out_video_path):
        remove_path([in_path_name, out_video_path])
        return False

    final_name = '{}_{}'.format(int(time.time()), video_file_name)

    url = video_qiniu.put(video_file_name, out_video_path)

     # 将视频的地址存入数据库
    if url:
        try:
            video_sub = VideoSub.objects.get(pk=video_sub_id)
            video_sub.url = url
            video_sub.save()
            return True
        except:
            return False
        finally:
            remove_path([in_path_name, out_video_path])
