def sum_of_squares( a , b ):
    return a**2 + b**2

num1 = int(input("enter first number : "))
num2 = int(input("enter second number : "))

result = sum_of_squares(num1 , num2)
print("sum of squares is : " , result)