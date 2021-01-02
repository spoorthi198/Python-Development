import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
user_choice = int(input('what do you want? type 0 for Rock, 1 for paper,2 for scissors\n'))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print('computer-choice:')
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print('yoy typed invalid number')
elif user_choice == 0 and computer_choice == 2:
    print('you win')
elif computer_choice == 0 and user_choice == 2:
    print('you lose')
elif computer_choice > user_choice:
    print('you lose')
elif user_choice > computer_choice:
    print('you win')
elif user_choice == computer_choice:
    print('game is draw')
