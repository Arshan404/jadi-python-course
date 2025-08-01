def is_even(n):
    '''
    returns true if the provided value is even
    '''

    return( n % 2 ==0 )

print(is_even(45))

print("------------------------")

def number_of_evens(nums):
    count = 0
    for n in nums:
        if n % 2 ==0:
            count += 1
    return count

count = number_of_evens([1,2,3,6,10,11])
print(count)

print("------------------------")

def number_of_evens(nums):
    count = 0
    for n in nums:
            if is_even(n):
                count += 1
    return count

count = number_of_evens([1,2,3,6,10,11])
print(count)

print("------------------------")

def number_of_evens(nums):

    def is_even(n):
        return( n % 2 ==0 )

    count = 0
    for n in nums:
            if is_even(n):
                count += 1
    return count

count = number_of_evens([1,2,3,6,10,11])
print(count)

print("------------------------")

def is_even(n):
    return n % 2 == 0

def any_even_in_list(nums):
    """
    returns true if any of numbers is even
    """
    has_even = False
    for n in nums:
        if is_even(n):
            has_even = True
    return has_even

my_numbers = [1, 2, 5, 8]
print(any_even_in_list(my_numbers))  

print("------------------------")

def is_even(n):
    return n % 2 == 0

def any_even_in_list(nums):
    """
    returns true if any of numbers is even
    """
    for n in nums:
        if is_even(n):
            return True
    return False
    

my_numbers = [1, 2, 5 , 8 ]
print(any_even_in_list(my_numbers)) 

print("------------------------")

def largest(nums):
    largest_number = nums[0]
    for n in nums:
        if largest_number < n:
            largest_number = n
    return largest_number

my_nums = [1,5,8,3,9,11,7]
largest_number = largest(my_nums)
print(largest_number)

print("------------------------")

def is_even(n):
    return n % 2 == 0

def get_odds(nums):
    odds = []
    for num in nums:
        if not is_even(num):
            odds.append(num)
    return odds

my_list = [1,2,6,8,2,5,3]
my_odds = get_odds(my_list)
print(my_odds)
print(len(my_odds))