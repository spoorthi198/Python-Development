from art import logo
import random
from game_data import data
from art import vs

print(logo)


def format_data(account):
    account_name = account["name"]
    account_title = account["description"]
    account_place = account["country"]
    return f"{account_name} a {account_title} from {account_place}"


def checker(guess, a_follower, b_follower):
    if a_follower > b_follower:
        return guess == 'a'
    else:
        return guess == 'b'


def game():
    is_guess_right = True
    score = 0
    account_b = random.choice(data)
    while is_guess_right:

        account_a = account_b
        account_b = random.choice(data)
        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}")

        print(vs)

        print(f"Against B: {format_data(account_b)}")

        # ask user for more follower
        guess = input("who has the more followers A or B?").lower()

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        # score tracking

        is_checker = checker(guess, a_follower_count, b_follower_count)

        if is_checker:
            score += 1
            print(f'you are right and your score is - {score}')
        else:
            is_guess_right = False

            print(f'you are wrong with final score-{score}')
        # game repetition
        # previous b becomes a


game()