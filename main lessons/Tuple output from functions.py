def is_even(n):
    return n % 2 == 0

def get_odds(nums):
    odds = []
    count = 0

    for num in nums:
        if not is_even(num):
            odds.append(num)
            count += 1

    return count,odds

my_list = [1,2,6,8,2,5,3]
odds_count , my_odds = get_odds(my_list)
print(odds_count , my_odds , sep="+") 


print("-------------------")


def jam_zarb(n1 , n2):
    jam = n1 + n2
    zarb = n1* n2

    return jam , zarb

#print(jam_zarb(3,4))

x , y = jam_zarb(3,4)
print(x)
print(y)

print("-------------------")

donations = {
    'jadi': 20,
    'sarah': 800,
    'hasan': 9,
    'far': 12,
}

def donations_analysis(don):
    total = 0
    count = 0
    max_person = ''
    max_amount = 0

    for name, amount in don.items():
        print(f"{name} donated {amount}")
        total += amount
        count += 1
        if amount > max_amount:
            max_amount = amount
            max_person = name

    average = total / count if count > 0 else 0
    return average, total, max_person

avg, total, max_person = donations_analysis(donations)

print(f"\nTotal donations: {total}")
print(f"Average donation is: {avg}")
print(f"Thanks to: {max_person}")
