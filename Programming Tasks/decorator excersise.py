import time

def measure_time(func):
    def wrapper(*args , **kwargs):
        start_time = time.time()        # شروع زمان‌سنج
        result = func(*args,**kwargs)  # اجرای تابع اصلی
        end_time = time.time()         # پایان زمان‌سنج
        elapsed = end_time - start_time
        print(f"Execution time: {elapsed:.6f} seconds")
        return result                   # برگرداندن خروجی اصلی تابع
    return wrapper

@measure_time
def create_list(n):
    return list(range(1,n+1))

n = int(input("Enter the value of n: "))
numbers = create_list(n)
print("Output:", numbers)
