l = [0 ,0.45 , 9 , -1]
new_l = []
for n in l:
    new_l.append(n*2)

print(new_l)

#list comprehension
new_l = [x*2 for x in l]  #لیستی که x ها دو برابر میشن به ازای هر x در l
neww_l = [n for n in l if n % 2 == 0]
print(new_l)
print(neww_l)

a = 5

if a % 2 == 0:
    res = "zoj"
else:
    res = "fard"

print(res)

#list comprehension
res2 = "fard " if a % 2 != 0 else "zoj"
print(res2)

w = [1,2,6,8,9]
new_w = ["zoj" if n % 2 == 0  else "fard" for n in w]
print(new_w)

new_d = ['hop' if n%3==0 else n for n in range(1,12)]
print(new_d)