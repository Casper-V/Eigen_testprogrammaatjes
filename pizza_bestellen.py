# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 15:23:24 2020

@author: Casper
"""


# pizza bestellen.
# De gebruiker voert een voor een de ingrediënten in, te kiezen uit een lijst.
# Als het ingrediënt al besteld is, wordt gevraagd of het ingrediënt extra veel moet worden gebruikt.
# Logischer zou misschien zijn een dictionary met {1:"gorgonzola", 2:"pineapple", etc.} te maken
# Dan voert de gebruiker het getal in en is er minder kans op spelfouten o.i.d.
available_toppings = ["gorgonzola", "pineapple", "ham", "bacon", "shrimp", "arugula", "mozzerella", "anchovies", "bell pepper", "pepper", "egg"]
print(f"You can choose from the following toppings: {available_toppings}")
toppings = []
active = True
while active:
    menu = "Which topping would you like for your pizza?\n"
    menu += "Input your toppings one by one and enter \'done\' once you're done.\n"
    pizza_order = input(menu)
    if pizza_order != "done":
        if pizza_order.lower() in available_toppings:
            if pizza_order.lower() not in toppings:
                toppings.append(pizza_order)
            else:
                print(f"You have already ordered {pizza_order}.")
                check_answer = input(f"Would you like to order a pizza with an extra portion of {pizza_order}? If so, type \'yes\'. ")
                if check_answer == "yes":
                    toppings.append(pizza_order)
        else:
            print("We didn\'t recognize this topping. Please check your spelling or order a different topping. Enter \'done\' once you\'re done.")
        continue
    else:
        active = False
        break
if len(toppings) == 0:
    print("You have ordered a pizza without any toppings.")
elif len(toppings) == 1:
    print("You have ordered a pizza with the following topping:")
else:
    print("You have ordered a pizza with the following toppings:")
for topping in toppings:
    print(topping.title())