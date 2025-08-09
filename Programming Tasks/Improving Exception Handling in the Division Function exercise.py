def divide(a,b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("error : ِDivision by zero is not permitted ! ")
        return None
    
while True:
    try:
        num1 = int(input("Enter first number : "))
        num2 = int(input("Enter second number : "))

        result = divide(num1 , num2)
        if result is not None:
            print("Result" ,result)
            break
    except ValueError:
        print("Error! please just enter numbers ! ")
    finally:
        print("The program executed successfully!")