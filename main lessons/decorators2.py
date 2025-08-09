def say_hello():
    import datetime
    now = datetime.datetime.now()
    minute = now.minute
    if minute % 2 == 0 :
        print("Hissss")
    else:
        print("salam! man Injam ")
        
say_hello()