# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma.\n ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
'''
print(names)
print(len(names))
name_pic = len(names)
#Write your code below this line 👇
random_pic = random.randint(0,name_pic-1)
print(f'you will be buying the meal today {names[random_pic]}')'''

person_pay_bill = random.choice(names)
print(f'person who will pay the bill is {person_pay_bill}')


