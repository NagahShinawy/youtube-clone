"""
created by Nagaj at 15/06/2021
"""
from channel import Channel
from video import Video


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
            self.save_to_activities({"activity": "like"})

    def iunlike(self, video: Video):
        """
        user can unlike a video
        :param video:
        :return:
        """
        if self in video.reacts:
            video.reacts.remove(self)
            self.save_to_activities({"activity": "unlike"})

    def comment(self, video: Video, acomment):
        """
         user can add comments on a video
        :param video: video to comment on
        :param acomment: user comment
        :return:
        """
        self.save_to_activities({"activity": {"comment": acomment}})
        video.comments.append(acomment)

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
