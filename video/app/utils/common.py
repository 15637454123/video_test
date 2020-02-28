# coding:utf-8
from django.conf import settings
import os
import time
import shutil


def handle_video(video_file, video_id, number):

    path = os.path.join(settings.BASE_DIR, 'app/dashboard/temp')
    name = '{}_{}'.format(int(time.time()), video_file.name)
    path_name = '/'.join([path, name])
    print(path_name)
    print(dir(video_file))
    temp_path = video_file.temporary_file_path()
    shutil.copyfile(temp_path, path_name)
