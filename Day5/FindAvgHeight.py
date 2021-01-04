# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

print( len(student_scores))
#Write your code below this row 👇
print(sum(student_scores))

avg_score = sum(student_scores)/len(student_scores)

print(round(avg_score))

print('*'*10)

temp = 0
count = 0
for score in student_scores:
  temp +=score
  count+=1
print(temp)
print(count)