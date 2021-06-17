"""
created by Nagaj at 15/06/2021
"""
import random

from channel import Channel
from comment import Comment
from video import Video
from react import Like, Love, Angry, Sad, CARE


class User:
    """
    class to handle youtube user actions
    """

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.activity_logs = []

    def __repr__(self):
        return f" <{self.username}:{self.email}> "

    def save_to_activities(self, activity):
        self.activity_logs.append(activity)

    def subscribe(self, channel: Channel):
        """
        user can subscribe a channel
        :param channel:
        :return:
        """
        if self not in channel.subscribers:
            channel.subscribers.append(self)
            channel.subscribes += 1
            self.activity_logs.append({"activity": "subscribe"})

    def unsubscribe(self, channel: Channel):
        """
        user can subscribe a channel
        :param channel:
        :return:
        """
        if self in channel.subscribers:
            channel.subscribers.remove(self)
            channel.subscribes -= 1
            self.save_to_activities({"activity": "unsubscribe"})

    def ilike(self, video: Video):
        """
        user can like a video
        :param video:
        :return:
        """
        if self not in video.reacts:
            video.reacts.append(self)
            react = random.choice([Like, Love, Angry, Sad, CARE])
            self.save_to_activities({"activity": react.show_react()})

    def iunlike(self, video: Video):
        """
        user can unlike a video
        :param video:
        :return:
        """
        if self in video.reacts:
            video.reacts.remove(self)
            self.save_to_activities({"activity": "unlike"})

    def icomment(self, video: Video, text):
        """
         user can add comments on a video
        :param video: video to comment on
        :param text: user comment
        :return:
        """
        comment_ = Comment(text)
        self.save_to_activities({"activity": {"comment": comment_}})
        video.comments.append(comment_)

    def delete_comment(self):
        pass
        # self.save_to_activities({"activity": {"delete-comment": acomment}})


class Youtuber(User):
    def __init__(self, username, email):
        super().__init__(username, email)
        self.channel = None

    def create_channel(self, channel):
        """
        youtube can create a channel(s)
        :param channel:
        :return:
        """
        self.channel = channel
