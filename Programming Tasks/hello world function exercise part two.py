"""
تابعی به نام greet بنویسید که یک نام به عنوان ورودی دریافت کند و "Hello, Name!" را چاپ کند. (به جای Name باید مقدار ورودی نمایش داده شود.)


ورودی نمونه:

Ali

خروجی مورد انتظار:

Hello, Ali!
"""

def greet(name):
    print(f"Hello, {name}!")

user_name = input("what is your name? ")
greet(user_name)