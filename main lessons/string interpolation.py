family_name = "mirmir"
name = "Jadi"
age = 45.458565

print("Hello" +" "+ name + " " + family_name ) # روش کثیف ترکیب رشته ها

print("Hello %s %s , you are %i" % (name , family_name ,age)) #روشی که در c وجو داشته

print("Hello {} {} , you are {}" .format(name , family_name , age)) # روش format string
print("Hello {1} {0} , you are {2}" .format(name , family_name , age))
print("Hello {1} {0} , you are {0}" .format(name , family_name , age))
print("Hello {name} {family} , you are {sen}" .format(name=name , family=family_name , sen=age))
print("Hello {name} {family} , you are {sen:1.1f}" .format(name=name , family=family_name , sen=age))

print(f"Hello {name} {family_name},you are {age:1.1f} years old") #روش نوین تر یا f string که از همه خواناتره