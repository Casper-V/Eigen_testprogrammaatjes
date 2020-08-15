# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 15:40:34 2020

@author: Casper
"""

# lijst met namen en lijst met voorbeelden van talen
# in php_variations kunnen evt. andere talen in hoofdletters worden toegevoegd
# niet helemaal waterdicht vanwege talen als JavaScript die worden geretourneerd als Javascript
names = ['bob', 'barry', 'cynthia', 'merol']
languages_to_select = ['python','c++', 'java', 'ruby', 'c#', 'php']
php_variations = ('php', 'Php', 'PHP')

# dictionary waarin de namen en talen aan elkaar worden gekoppeld, willekeurig ingevuld
favorite_languages = {
    names[0]: languages_to_select[0],
    names[1]: languages_to_select[1],
    names[2]: languages_to_select[2],
    names[3]: languages_to_select[5],
    }

# input van de gebruiker
user_name = str(input('Enter your user name: '))
while user_name.lower() in names:
    user_name = str(input('This user name already exists. Enter a different user name: '))
print(f"Hi, {user_name}! Which of the following languages is your favorite? You can add a different language.")

for language in languages_to_select:
    if language in php_variations:
        language = language.upper()
    else:
        language = language.title()
    print(f"{language}")
my_favorite = str(input("My favorite is: ")).lower()

# input wordt toegevoegd aan lijst en dictionary, met lower case om later te kunnen sorteren
# dictionary wordt op alfabetische volgorde gezet om de output netjes weer te geven
names.append(user_name.lower())
favorite_languages[names[-1]] = my_favorite
alphabetically = dict(sorted(favorite_languages.items()))

# output van het programma
for fav in alphabetically:
    if alphabetically[fav] in php_variations:
        print(f"{fav.title()}\'s favorite programming language is {alphabetically[fav].upper()}.")
    else:
        print(f"{fav.title()}\'s favorite programming language is {alphabetically[fav].title()}.")

# alternatieve notatie output van het programma
# for name, favorite in alphabetically.items():
#     if favorite in php_variations:
#         print(f"{name.title()}\'s favorite programming language is {favorite.upper()}.")
#     else:
#         print(f"{name.title()}\'s favorite programming language is {favorite.title()}.")

# tot slot vaststellen hoeveel talen in totaal zijn genoemd met de gebruiker erbij
# set() retourneert alleen de unieke waarden
length = len(set(favorite_languages.values()))
print(f"The following {length} languages are mentioned as favorites:")
for language in set(favorite_languages.values()):
    if language in php_variations:
        print("PHP")
    else:
        print(language.title())

# alle gebruikers noemen
print("The following users have indicated their favorite language:")
for name in sorted(favorite_languages):
    print(name.title())
    
# optionele uitbreiding voor meerdere talen als lijst in dictionary:
# all_users = ['bob', 'harry', 'mary', 'boris', 'barry', 'cynthia', 'merol']
# names_in_dictionary = ['bob', 'barry', 'cynthia', 'merol']
# languages_to_select = ['python','c++', 'java', 'ruby', 'c#', 'php']
# favorite_languages = {
#     names_in_dictionary[0]: [languages_to_select[0], languages_to_select[3]],
#     names_in_dictionary[1]: [languages_to_select[1], languages_to_select[3]],
#     names_in_dictionary[2]: [languages_to_select[2]],
#     names_in_dictionary[3]: [],
#     }

# for name, languages in favorite_languages.items():
#     if len(languages) > 1:
#         print(f"{name.title()}'s favorite languages are: ")
#     elif len(languages) == 1:
#         print(f"{name.title()}'s favorite language is: ")
#     elif len(languages) == 0:
#         print(f"{name.title()} has no favorite language.")
#     for language in languages:
#         print(language.title())