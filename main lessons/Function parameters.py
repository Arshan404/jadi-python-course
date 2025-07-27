def sum_of_two_numbers(a,b):
    res = a + b
    return res

n1 = 4
n2 = 6

print(sum_of_two_numbers(n1,n2))

res =sum_of_two_numbers(n1,n2)
print(res)

print("-----------------------")

def print_times(name,n=1):               #اینجا پارامتر اینکه چندبار چاپ کنه رو بای دیفالت براش مشخص کردیم که یکباره و اگه در اخر که فراخوانیش میکنیم مشخص نکنیم مقدارشو برامون ارور نمیده
    '''
    print name , n timess,

    parameters
    ---------

    name:string
        what to print.
    n : int
        how many times to print.
    returns
    -------
    none.
    '''
    for i in range(n):
        print(name)

print_times("jadi")

print("-----------------------")

def tavan(n,t=2):
    javab = 1
    for i in range(t):
        javab *= n      #javab = javab*n
    return javab

print(tavan(2,6))

print("-----------------------")

def sum_of_two(n1,n2=10):
    return n1+n2

print(sum_of_two(1,45))
print(sum_of_two("jadi" , "jan"))
print(sum_of_two("jadi" , "10"))
print(sum_of_two("jadi"))
