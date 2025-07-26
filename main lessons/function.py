def hello(name):
    for i in range(len(name)):  #به تعداد طول اسم چاپ میکنه
        print(f"oh hello {name}")

hello('jadi')

print("-------------------")

def say_hello_n_times(name , n ):
    '''
    this function says hello to the name,n times.
    '''
    for i in range(n):  
        print(f"oh hello {name}")

say_hello_n_times('jadi' ,3)
say_hello_n_times("mosi" ,5)

print("-------------------")

def sum_of_two_numbers( a , b ):
    res = a + b
    print(res)

sum_of_two_numbers(4,5) 

print("-------------------")

def sum_of_two_numbers( a , b ):
    res = a + b
    return res

print(sum_of_two_numbers(4,5)) 
print(f"sum of 2 , 4 is {sum_of_two_numbers(2,4)}")

print("-------------------")

def chants_toosh( s , c):
    '''
    gets a string and character and returns the numbers that character repeattions in that string
    '''
    counter = 0
    for this_character in s:
        if this_character == c :
            counter +=1
    return(counter)
name = "jadijan"
print(f"{name} has {chants_toosh(name , "a")} a")

print("-------------------")

def chants_toosh( s , c):
    '''
    gets a string and character and returns the numbers that character repeattions in that string
    '''
    counter = 0
    for this_character in s:
        if this_character == c :
            counter +=1
    return(counter)

name = "jadijan"
show = chants_toosh( name , "a")

print(f"{name} has {show} a")
