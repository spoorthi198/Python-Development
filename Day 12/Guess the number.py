import random

numbers = [25, 36, 47, 52, 65, 79, 88, 92]
Secret_number = random.choice(numbers)
print(Secret_number)
print('welcome to number guessing game')
print("i'm thinking of a number between 1 and 100")
level = input("choose difficulty level 'easy' or 'hard'").lower()
global find_number


def guess_number(count):
    count = count
    find_number = False
    while not find_number:
        guess = int(input('make a guess:?'))
        if guess == Secret_number:
            print('you got it!')
            print(f'guessed the secret number: {Secret_number}')
            find_number = True
            break
        elif guess > Secret_number:
            print('Number is too high')
            print('guess again')
        elif guess < Secret_number:
            print('Number is too low')
            print('guess again')

        count -= 1
        print(f'you have {count} guess left')

        if count == 0:
            find_number = True
            print('you ran out of all guess')


if level == 'easy':
    print('you have 3 attempts to guess the number')
    guess_number(3)

elif level == 'hard':
    print('you have 2 attempts to guess the number')
    guess_number(2)






