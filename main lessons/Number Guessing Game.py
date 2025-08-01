import random

def welcome():
    print("welcome to this funny Game")
    print("I will guess a  number between 1 to 100 and")
    print("you have to guess it...")
    print("go go go")
    print()

def finish(number , count):
    print("good game")
    print(f"my number was {number} and you found it in {count} guess!!")
    print()
    answer = input("do you want to play again? (Y/N)  ")
    if answer.upper() in  ["Y" , 'YES' , 'ARE']:
        return True
    else:
        return False

def win(computer_number , guess):

    if computer_number == guess:
        return True
    else:
        return False


def answer(computer , user):

    if computer > user :
        return 'My number is larger'
    if computer < user :
        return 'ohhh.you went sooo large! mine is smaller'
    
    return 'ohh! you won ! Good guess'

    '''
    if computer > user :
        res = 'My number is larger'
    elif computer < user :
        res = 'ohhh.you went sooo large! mine is smaller'
    else:
        res = 'ohh! you won ! Good guess'

    return res
    '''

def get_a_guess():
    ans = input("what is your guess? ")
    return int(ans)


welcome()
countinue_playing = True

while(countinue_playing):

    #computer number between 1 to 20
    computer_random = random.randint(1,20)

    #start with a wrong guess
    guess = 0

    count = 0


    while (not win(computer_random,guess)):
        guess = get_a_guess()
        count += 1
        print(answer(computer_random , guess))

    countinue_playing = finish(computer_random , count)