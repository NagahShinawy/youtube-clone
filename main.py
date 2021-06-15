"""
created by Nagaj at 15/06/2021
"""
from channel import Channel
from playlist import Playlist
from user import Youtuber
from video import Video

TIMES = 100
SPACE = "\t"


def main():
    """
    entry point for the app
    :return:
    """
    tim = Youtuber("Tim", "tim@gmail.com")
    techtim = Channel("Tech With Tim", tim)

    # ############ ############  test create channel ############ ############ ############ ###########
    tim.create_channel(techtim)
    print(techtim)
    print(techtim.is_verified)
    print(techtim.likes)
    print(techtim.subscribes)

    # ############ ############  test create playlist ############ ############ ############ ###########
    print("#" * 100)
    python_4_everyone = Playlist("Python For Everyone")
    django_crash_course = Playlist("Django WEb Framework")
    flask_tutorials = Playlist("Flask Micro")
    techtim.add_playlist(python_4_everyone)
    techtim.add_playlist(flask_tutorials)
    techtim.add_playlist(django_crash_course)
    print(techtim.playlists)
    print("#" * 100)

    # ############ ############ test upload videos ############ ############ ############ ###########
    numpy = Video("Numpy for math operations")
    techtim.upload(numpy)
    django_into = Video("Django Into. What is Django")
    django_models = Video("Models in Django. What is ORM?")
    whats_pandas = Video("What is Pandas Library?")
    create_flask_app = Video("Create Flask App")
    flask_form = Video("Flask Form")
    flask_mongo = Video("Flask With Mongo")
    flask_api = Video("Rest APi with Flask")
    techtim.upload(django_into)
    print(techtim.videos)
    print(techtim.playlists)
    techtim.save_to_playlist(django_into, django_crash_course)
    techtim.save_to_playlist(django_models, django_crash_course)

    techtim.save_to_playlist(create_flask_app, flask_tutorials)
    techtim.save_to_playlist(flask_api, flask_tutorials)
    techtim.save_to_playlist(flask_mongo, flask_tutorials)
    techtim.save_to_playlist(flask_form, flask_tutorials)

    print(techtim.playlists)

    print("#" * 100)
    # ############ ############ test magic methods in playlist class ############ ############ ############ ###########
    for start, video in enumerate(django_crash_course, start=1):
        print(f"{start}-{video}")

    print(django_into in django_crash_course)

    print(whats_pandas in flask_tutorials)
    print(whats_pandas in django_crash_course)

    print(django_models in flask_tutorials)
    print(django_models in django_crash_course)

    print("#" * 100)
    # ############ ############ test magic methods in channel class ############ ############ ############ ###########
    for playlist in techtim:
        print(playlist)
    print("|" * 50)
    for start, playlist in enumerate(techtim, start=1):
        print(f"{start}-{playlist}")
        for counter, video in enumerate(playlist, start=1):
            print(f"{SPACE * 2}{counter}-{video}")
        print("#" * TIMES)
    # ############ ############ test delete video, playlist ############ ############ ############ ###########
    techtim.delete_video(django_models)
    print(techtim.videos)
    print(techtim.playlists)
    techtim.delete_playlist(flask_tutorials)
    print(techtim.playlists)
    techtim.delete_video(numpy)
    print(techtim.videos)


if __name__ == "__main__":
    main()
