"""
created by Nagaj at 17/06/2021
"""
from abc import ABC


class React(ABC):
    EMOTION = ""

    @classmethod
    def show_react(cls):
        print(cls.EMOTION)
        return cls.EMOTION


class Like(React):
    EMOTION = "LIKE"


class Love(React):
    EMOTION = "LOVE"


class Angry(React):
    EMOTION = "ANGRY"


class Sad(React):
    EMOTION = "SAD"


class CARE(React):
    EMOTION = "CARE"
