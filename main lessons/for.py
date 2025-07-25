my_list = [2,4,6,8,'a']

for this_item in my_list:
    print(this_item)
    print(f"*2 = {this_item*2}")
print("ended")

my_list_2 = [1,2,4,5,6,7,9,11,10,12]
count = 0

for a in my_list_2 :
    if a % 2 == 0 :
        count +=1
        print(a)
    else:
        print(f"{a} is odd")
print(f"we had {count} even numbers")