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

    def __repr__(self):
        return f" <{self.username}:{self.email}> "

    def subscribe(self, channel: Channel):
        """
        user can subscribe a channel
        :param channel:
        :return:
        """
        if self not in channel.subscribers:
            channel.subscribers.append(self)
            channel.subscribes += 1

    def unsubscribe(self, channel: Channel):
        """
        user can subscribe a channel
        :param channel:
        :return:
        """
        if self in channel.subscribers:
            channel.subscribers.remove(self)
            channel.subscribes -= 1

    def like(self, video: Video):
        """
        user can like a video
        :param video:
        :return:
        """
        if self not in video.reacts:
            video.reacts.append(self)

    def unlike(self, video: Video):
        """
        user can unlike a video
        :param video:
        :return:
        """
        if self in video.reacts:
            video.reacts.append(self)

    @staticmethod
    def comment(video: Video, comment_):
        """
         user can add comments on a video
        :param video: video to comment on
        :param comment_: user comment
        :return:
        """
        video.comments.append(comment_)

    def delete_comment(self):
        pass


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
