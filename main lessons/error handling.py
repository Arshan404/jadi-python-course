try:
    prit("this is a test")
except:
    print("natonestam ke")

print("----------------")

def divisi(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("b can not be 0")
        return None
    except Exception as e:
        print(f"Another error :{e}")
        return None

print(divisi(1,2))
print(divisi(3,0))
print(divisi("a",True))

print("----------------")

try:
    f = open("/tmp/chertpert")
except FileNotFoundError:
    print("file does not found")
except Exception as e:
    print(f"another error: {e}")

print("----------------")

def division(a,b):
    try:                     #try this
       r = a/b
    except Exception as e:   #show exceptions
        print(f"had error : {e}")
        r = None
    else:                    #will run if no exception happens
       print(r)
    finally:                 #will be done in any case
        return r

division(1,2)