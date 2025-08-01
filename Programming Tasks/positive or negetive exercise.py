def  is_positive(number):
    return number >= 0

user_input = int(input("Enter a number : "))

result = is_positive(user_input)
print(result)