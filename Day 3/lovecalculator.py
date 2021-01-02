# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


T_count = name1.count('t')
R_count = name1.count('r')
U_count= name1.count('u')
E_count = name1.count('e')



L_count = name1.count('l')
O_count = name1.count('o')
V_count= name1.count('v')
E_count = name1.count('e')






T_count1 = name2.count('t')
R_count1= name2.count('r')
U_count1= name2.count('u')
E_count1 = name2.count('e')



L_count1 = name2.count('l')
O_count1 = name2.count('o')
V_count1= name2.count('v')
E_count1 = name2.count('e')

Total_true_count = T_count +T_count1 + R_count+R_count1++U_count1+E_count1

Total_love_count = L_count+L_count1+O_count+O_count1+V_count+V_count1+E_count+E_count1
print(f'your love score is :{Total_true_count} {Total_love_count}%')

love_score=str(Total_true_count) + str(Total_love_count)

love_score1 = int(love_score)

# Love Scores less than 10 or greater than 90, the message should be:

if love_score1 < 10 or love_score1 > 90:
  print(f'your score is {love_score1}, you go together like coke and mentos.')
if love_score1 > 40 and love_score1 < 60:
  print(f'your score is {love_score1},  you are alright together.')
else:
  print(f'your love score is {love_score1}')
