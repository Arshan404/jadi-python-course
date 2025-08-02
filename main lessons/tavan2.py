def tavan_2(x):
    return x ** 2

a = [3,4,2,8]

for i in range (len(a)):
    a[i] = tavan_2(a[i])

print(a)


print("-----------------")

def tavan_2(x):
    return x ** 2

a = [3,4,2,8]

tavan_a = map(tavan_2 , a )

print(tavan_a)
print(list(tavan_a))

print("-----------------")

a = [3,4,2,8]
tavan_a = map(lambda x: x**2 , a)
print(list(tavan_a))

print("-----------------")

def is_ashari(x):
    return x != int(x)

a = [5,6.2,8,9.1,8,4,2.9]
print(list(filter(is_ashari , a)))

print("-----------------")

a = [5,6.2,8,9.1,8,4,2.9]
print(list(filter(lambda x: x != int(x) , a)))

print("-----------------")

names = ['jadi' , 'hasan' , 'sara' , 'sina' , 'masoome']

short_names = filter(lambda s: len(s) <= 4 , names)

for name in short_names:
    print(name)

