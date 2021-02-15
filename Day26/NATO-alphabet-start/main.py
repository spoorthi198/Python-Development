student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data=pandas.read_csv('nato_phonetic_alphabet.csv')
stud_dict=data.to_dict()
stud_dict_DF= pandas.DataFrame(stud_dict)

new_dict = {row.letter:row.code for (index, row) in stud_dict_DF.iterrows()}
print(new_dict)

# 2. Create a list of the phonetic code words from a word that the user inputs.

user_choice=input('enter the word?').upper()

new_list = [new_dict[letter] for letter in user_choice]
print(new_list)