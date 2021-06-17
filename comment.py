"""
created by Nagaj at 17/06/2021
"""


class Comment:

    comments = []

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f"Comment(text={self.text})"

    def save(self):
        if self not in self.comments:
            self.comments.append(self)

    def delete(self):
        if self in self.comments:
            self.comments.remove(self)
