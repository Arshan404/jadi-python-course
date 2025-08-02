def zarb(*args):
    res = 1
    for i in args:
        res *= i 
    return res

b = zarb(3,4,5,6)
print(b)

print("--------------------")

def masahat(**kwargs):
    print(kwargs)

masahat(tool=8, ertefa=7)

print("--------------------")

def calculate_masahat(**kwargs):
    print(f"kwargs is : {kwargs}")
    if 'tool' in kwargs:
        return kwargs['tool'] * kwargs['ertefa']
    if 'shoa' in kwargs:
        return kwargs['shoa'] * 3.1415926 *kwargs['shoa']
    
print(calculate_masahat(tool = 3 , ertefa = 8))