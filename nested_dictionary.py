# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 16:28:03 2020

@author: Casper
"""


artist = {
    'bob dylan': {'age': 79, 'debut album': 1962, 'sex': 'male'},
    'bruce springsteen': {'age': 71, 'debut album': 1973, 'sex': 'male'},
    'nancy sinatra':  {'age': 80, 'debut album': 1962, 'sex': 'female'},
    }

# info is hieronder de informatie in de dictionary artist
for name, info in artist.items():
    age = info['age']
    debut_album = info['debut album']
    sex = info['sex']
    if sex == 'male':
        print(f"{name.title()} is {age} years old. His first album was released in {debut_album}.")
    elif sex == 'female':
        print(f"{name.title()} is {age} years old. Her first album was released in {debut_album}.")

# zonder de naam te noemen; alleen de values van artist worden gebruikt
for info in artist.values():
    age = info['age']
    debut_album = info['debut album']
    sex = info['sex']
    if sex == 'male':
        print(f"He is {age} years old. His first album was released in {debut_album}.")
    elif sex == 'female':
        print(f"She is {age} years old. Her first album was released in {debut_album}.")

# nog een voorbeeld
friends = {
    'friend_01': {
                'first_name': 'john',
                'last_name': 'travolta',
                'occupation': 'actor',
                'sex': 'male',
                },
    'friend_02': {
                'first_name': 'mark',
                'last_name': 'lanegan',
                'occupation': 'songwriter',              
                'sex': 'male',
                },
    'friend_03': {
                'first_name': 'pat',
                'last_name': 'barker',
                'occupation': 'author',              
                'sex': 'female',
                },
    }

for friend, info in friends.items():
    full_name = str(info['first_name']) + ' ' + str(info['last_name'])
    occupation = info['occupation']
    sex = info['sex']
    if sex == 'male':
        print(f"{full_name.title()} is a famous {occupation}. Isn't he great?")
    if sex == 'female':
        print(f"{full_name.title()} is a famous {occupation}. Isn't she great?")