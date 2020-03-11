# coding: utf-8

from django.db import  models
from .auth import ClientUser
from .viedo import Video


class Comment(models.Model):

    content = models.TextField()
    video = models.ForeignKey(Video, related_name='video_comment', on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(ClientUser, related_name='user_comment', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.content

    def data(self):
        return {
            'id': self.id,
            'content': self.content,
            'video_id': self.video.id,
            'user_id': self.user.id,
            'username': self.user.username
        }
