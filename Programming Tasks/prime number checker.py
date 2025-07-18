import time 
start_time = time.time()

def is_prime(n):
    avval = True
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            avval = False
            break
    return avval 

prime_count = 0
last_prime_number=0

for i in range(1,100001):
    if is_prime(i):
        last_prime_number = i
        prime_count = prime_count + 1
        #print(i)  
print("last prime number is", last_prime_number)
print("we had",prime_count,"prime numbers")
print("process finished ---%s seconds ---" % (time.time() - start_time))
