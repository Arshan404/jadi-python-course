class classname():
    def __init__(self , param1):
        self.param1 = param1
        print("object created")
    def say_hello(self):
        print(f"hello")

t = classname(5)
print(t.param1)
print(t.say_hello())
print(type(t))