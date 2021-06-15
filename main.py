"""
created by Nagaj at 15/06/2021
"""
from channel import Channel
from user import Youtuber

TIMES = 100


def main():
    """
    entry point for the app
    :return:
    """
    tim = Youtuber("Tim", "tim@gmail.com")
    techtim = Channel("Tech With Tim", tim)

    # ############ ############ ############ ############ ############ ###########
    tim.create_channel(techtim)
    print(techtim)
    print(techtim.is_verified)
    print(techtim.likes)
    print(techtim.subscribes)


if __name__ == "__main__":
    main()
