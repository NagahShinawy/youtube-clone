"""
created by Nagaj at 15/06/2021
"""
from video import Video
from playlist import Playlist


class Channel:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.playlists = []
        self.videos = []
        self.likes = 0
        self.subscribes = 0
        self.is_verified = False

    def __repr__(self):
        return f"{self.name}\n{self.subscribes} Subscribes"

    def verify(self):
        """
        verify a channel
        :return:
        """
        self.is_verified = True

    def increment_likes(self):
        """
        when user like on a a video, likes should be increment
        :return:
        """
        self.likes += 1

    def increment_subscribes(self):
        """
           when user subscribe a channel , subscribe should be increment
           :return:
        """
        self.subscribes += 1

    def upload(self, video: Video):
        """
        channel uploads videos
        :param video:
        :return:
        """
        pass

    def save_to_playlist(self, video: Video, playlist: Playlist):
        """
         channel saves videos to playlists
        :param video: video obj to be saved to a playlist
        :param playlist: playlist obj that saves the video
        :return:
        """
    def remove_video(self, video: Video):
        pass

    def remove_playlist(self, playlist: Playlist):
        pass
