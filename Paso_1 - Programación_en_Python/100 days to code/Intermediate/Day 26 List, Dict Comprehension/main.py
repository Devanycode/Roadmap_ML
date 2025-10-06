new_list = [x * 2 for x in range(1,5)]
print(new_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name.upper() for name in names if len(name) >= 5]
print(short_names)

import random 
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)

students_winners = {student:result for (student, result) in students_scores.items() if result >= 60}
print(students_winners)


import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
student_data_frame = pandas.DataFrame(student_dict)
for (index, row) in student_data_frame.iterrows():
    pass
    # print(row)

# Proyecto Nato Phonetic
nato_phonetic_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
# Created phonetic dict 
nato_phonetic_dict = {nato.letter:nato.code for (index, nato) in nato_phonetic_csv.iterrows()}

user_word = input("Enter a word: ").upper()   # Porque las claves del diccionario están en mayúsculas

for word in user_word:
    if word in nato_phonetic_dict.keys():
        print(nato_phonetic_dict[word])
phonetic_list = [nato_phonetic_dict[word] for word in user_word]
print(phonetic_list)

# TODO 2. Luego crear una lista con una palabra que ingresa el usuario