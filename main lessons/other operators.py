for i in range(10):
    for j in range(10):
        print(i*j , end="\t")
    print()

print("-------------------------")

for i in range (2, 16 ,2):
    print(i , end=" ")
    print("\n")

print("-------------------------")

l = 'jadi'
for i in range (len(l)):
    print(i , l[i])
print(enumerate(l))
for i , a in enumerate(l):
    print(i , a )

print("-------------------------")

esm = ['jadi','ali','sara']
famil = ['mirmir','par', 'zad']
sen = [45 , 21 , 12]

for x in zip(esm,famil,sen):
    print(x)

print("-------------------------")

s = 'sbcd'

if 'j' in s:
    print("bood")
else:
    print("nabood")

print("-------------------------")

p = {
    'jadi':{'sen' : 45 , 'ghad':180},
    'sarah':{'sen' : 12 , 'ghad' : 190}
}

if 'jadi' in p:
    print("I HAVE")

print("-------------------------")

names = ['jadi' , 'ali' 'sarah']
people = {
    'jadi':{'sen' : 45 , 'ghad':180},
    'sarah':{'sen' : 12 , 'ghad' : 190}
}

for name in names:
    if name in people:
        # we have this person
        # lets print the sen
        print(f"I have {name} and sen is {people[name]['sen'] }") 
    else:
        print(f"I have no data for {name}")

print("-------------------------")

print(max(1,2,3,9))
print(min(1,2,3,9))

print("-------------------------")

from random import randint

print(randint(1,6))

print("-------------------------")

from random import randint
a = input("ye add bedeh:")
a = int(a)
print(a*2) 

print("-------------------------")

from random import randint

javab = randint(1,6)

i = input("chand bood?")
i = int(i)

if (i == javab):
    print("wooow...")
else:
    print(f"na! mal man {javab} bood " )