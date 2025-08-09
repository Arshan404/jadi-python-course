import time

def is_it_zoj():
    import datetime
    now = datetime.datetime.now()
    minute = now.minute
    return minute % 2 == 0


def say_hello():
    if is_it_zoj():
        print("Hissss")
    else:
        print("salam! man Injam ")

def say_bye():
    if is_it_zoj():
        print("bye bye!")

say_hello()
say_bye()
