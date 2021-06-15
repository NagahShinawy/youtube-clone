"""
created by Nagaj at 15/06/2021
"""


class Playlist:

    def __init__(self, title):
        self.title = title
        self.videos = []

    def __repr__(self):
        return f" <{self.title} {len(self.videos)}> "

    def __getitem__(self, item):
        return self.videos[item]

    def __contains__(self, item):
        return item in self.videos

    def add_video(self, video):
        if video not in self.videos:
            self.videos.append(video)
