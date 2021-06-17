"""
created by Nagaj at 17/06/2021
"""


class Comment:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f"Comment(text={self.text})"
