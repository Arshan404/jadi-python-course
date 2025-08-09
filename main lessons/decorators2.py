def run_on_zoj(f):
    import datetime
    now = datetime.datetime.now()
    minute = now.minute
    if minute % 2 == 0 :
        f()
    else:
        print('hissss')


def say_hello():
        print("salam! man Injam ")

def say_bye():
        print("bye bye!")

run_on_zoj(say_hello)
run_on_zoj(say_bye)
