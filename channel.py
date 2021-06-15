"""
created by Nagaj at 15/06/2021
"""
from playlist import Playlist
from video import Video


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

    def __getitem__(self, item):
        return self.playlists[item]

    def __contains__(self, item):
        return item in self.playlists

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
        if video not in self.videos:
            self.videos.append(video)

    def create_playlist(self, playlist: Playlist):
        if playlist not in self.playlists:
            self.playlists.append(playlist)

    def save_to_playlist(self, video: Video, playlist: Playlist):
        """
         channel saves videos to playlists
        :param video: video obj to be saved to a playlist
        :param playlist: playlist obj that saves the video
        :return:
        """
        self.upload(video)
        if playlist in self.playlists:
            playlist.add_video(video)
            video.playlist_related = playlist

    def delete_video(self, video: Video):
        if video in self.videos:
            self.videos.remove(video)
            video.playlist_related.videos.remove(video)

    def delete_playlist(self, playlist: Playlist):
        if playlist in self.playlists:
            self.playlists.remove(playlist)
