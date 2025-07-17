"""
یک دیکشنری به نام fruit_prices بسازید که شامل قیمت‌های میوه‌ها باشد. قیمت‌ها به شرح زیر است:

apple: 1500
banana: 1000
orange: 1200

سپس کدی بنویسید که قیمت banana را تغییر داده و به 1100 تغییر دهد و apple را به طور کلی حذف کند. در آخر این دیکشنری را چاپ کنید.

"""

# ساخت دیکشنری اولیه
fruit_prices = {
    "apple": 1500,
    "banana": 1000,
    "orange": 1200
}

# تغییر قیمت banana به 1100
fruit_prices["banana"] = 1100

# حذف apple از دیکشنری
del fruit_prices["apple"]

# چاپ دیکشنری نهایی
print(fruit_prices)
