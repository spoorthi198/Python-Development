# names = ['alex', 'beth', 'caroline', 'dave', 'elanor', 'freddie']
# import random
# student_score = {student:random.randint(30,100) for student in names}
# passed_score = {student:score for (student,score) in student_score.items() if score > 60}

sentence = "what is your name"

new_sentence = sentence.split(" ")
print(new_sentence)

new_dict = {word : len(word) for word in new_sentence}
print(new_dict)

weather_c = {
    "Monday" : 12,
    "Tuesday" : 14,
    "wednesday": 15,
    "Thursday" : 14,
    "Friday" : 21,
    "Saturday" : 22,
    "Sunday" : 24
}

weather_f = {day:(temp_c* 9/5)+32 for (day,temp_c) in weather_c.items()}
print(weather_f)