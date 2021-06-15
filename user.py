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
        return f"<{self.username}><{self.email}>"

    def subscribe(self, channel: Channel):
        """
        user can subscribe a channel
        :param channel:
        :return:
        """
        pass

    def like(self, video: Video):
        """
        user can like a video
        :param video:
        :return:
        """
        pass

    def comment(self, video: Video):
        """
        user can add comments on a video
        :param video:
        :return:
        """
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
