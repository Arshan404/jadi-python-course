def is_even(n):
    if n % 2 ==0:
        return True
    else:
        return False
    
while True:
    user_input = input("enter a number or 'exit' for ending program :  ")

    if user_input =='exit':
        print("program just finished")
        break

    try:
        n = int(user_input)
        print(is_even(n))
    except ValueError:
        print("please enter a integer number or type ' exit ' to shut down program ")

