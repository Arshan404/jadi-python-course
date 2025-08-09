def add(a,b):
    result = a + b
    return result
b = add(3,4)
print(b)

print("-------------------")

def say_hello():
    print("hello there")

say_hello()
my_function = say_hello
my_function()
print(my_function is say_hello)
say_hello()
my_function()

print("-------------------")

def add(a,b):
    return a+b
def calculate(a,b,f):
    return f(a,b)
print(calculate(1,3,add))


def say_hello():
    print("hello there")

def do_twice(what_to_call):
    what_to_call()
    what_to_call()

do_twice(say_hello)

print("-------------------")

def calculate(a,b,what_to_do):
    def add(a,b):
        return a+b
    def zarb(a,b):
        return a*b
    
    if what_to_do == 'add':
        return add(a,b)
    if what_to_do =='zarb':
        return zarb(a,b)
    
result = calculate(3,4,'zarb')
print(result)