"""
created by Nagaj at 15/06/2021
"""


class Video:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.tags = []
        self.reacts = []
        self.comments = []
        self.belongs_to_playlist = None

    def __repr__(self):
        return f"Video(title={self.title}, reacts={len(self.reacts)}, comments={len(self.comments)})"
