"""
created by Nagaj at 15/06/2021
"""
from channel import Channel
from playlist import Playlist
from user import Youtuber, User
from video import Video

TIMES = 100
SPACE = "\t"


def main():
    """
    entry point for the app
    :return:
    """
    john = User("John", "jo@test.com")
    tim = Youtuber("Tim", "tim@gmail.com")
    techtim = Channel("Tech With Tim", tim)
    dogs = Channel("Me and Dog", tim)

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

    print("#" * 50, "Magic Methods", "#" * 50)
    # ############ ############ test magic methods in channel class ############ ############
    print(techtim.playlists)
    print(techtim[:-1])
    print(techtim[::-1])
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

    # ############ ############ test likes, comments, subscribe ############ ############ ############ ###########
    tim.comment(flask_form, "this is clear concepts of flask form")
    tim.comment(flask_form, "hope to upload more videos of flask")
    print(flask_form)
    tim.ilike(flask_form)
    tim.subscribe(techtim)
    print(flask_form)
    print(techtim.subscribers)
    print(techtim.subscribes)
    print(techtim.likes)
    print("#" * TIMES)
    # ############ ############ test unlikes, subscribe,  delete comments, ######### ############ ############
    tim.ilike(numpy)
    tim.ilike(numpy)
    tim.ilike(numpy)
    tim.ilike(numpy)
    tim.ilike(numpy)
    print(numpy)
    tim.iunlike(numpy)
    print(numpy)
    #######
    john.subscribe(dogs)
    tim.subscribe(dogs)
    print(dogs)

    # ############ ############ test history, ######### ############ ############
    print(tim.activity_logs)


if __name__ == "__main__":
    main()


# todo: 1- can creator subscribe him self?
# todo: 2- genreic module for toggle like, unlike, subscribe, unsubscribe
# todo: 3- history
# todo: 3- comment class
# todo: 3- implement delete comment
