my_tupple = (8,9,'jadi' , 9.1)

for bibi in my_tupple:
    print(bibi)

my_tupple_2 = (8,9,'jadi',[1,2,3] , 9.1)

for bibi in my_tupple_2:
    print(bibi)

people = (('jadi' , 45) , ('sina' , 12) , ('farzaneh' ,18))
for person in people:
    name, sen = person
    print(f"{name} is {sen} years old")


for c in 'jadi is fun':
    print(c)

people_2 ={
    "jadi" : (45,180) , "sina" : (12 , 120) , 'farzaneh' : (30 , 190)
}
for person in people_2 :
    print(person , people_2[person])
    print(person , people_2[person][0])

for person in people_2.items():
    print(person)

for person , data in people_2.items():
    print(f"{person} -> {data}")