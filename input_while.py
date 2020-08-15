# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 18:59:34 2020

@author: Casper
"""


# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 18:55:47 2020

@author: Casper
"""
# prompt = "Hello there!\nWhats your name? "
# name = input(prompt)
# print(f"Hello, {name}")

# age = input("How old are you? ")
# age = int(age)
# if age >= 18:
#     print("I like you!")

# number = int(input("Geef een getal op: "))
# if number % 2 == 0:
#     print(f"Het getal {number} is even.")
# else:
#     print(f"Het getal {number} is oneven.")
# if number % 10 == 0:
#     print(f"{number} is een veelvoud van tien.")
# else:
#     print(f"{number} is geen veelvoud van tien.")

# # vraag bij restaurant of er plek is
# number_of_seats = int(input("How many seats do you want to reserve? "))
# if number_of_seats <= 8:
#     print (f"No problem. We have a table for {number_of_seats} seats ready for you.")
# else:
#     print ("Sorry, you will have to wait.")

# # herhalen wat de gebruiker invoert
# actief = True
# prompt = "Typ wat tekst. Ik zal de tekst herhalen.\nAls je wilt stoppen, typ je \'opnieuw\'.\n"
# papegaai = ""
# while actief:
#     papegaai = input(prompt)
#     if papegaai == "opnieuw":
#         print("Tot ziens.")
#         actief = False
#         break
#     else:
#         print(papegaai)

# # even getallen t/m 20.
# # Als het getal niet even is, wordt continue geactiveerd en wordt er dus niets geprint.
# huidig_getal = 0
# while huidig_getal < 20:
#     huidig_getal += 1
#     if huidig_getal % 2 != 0:
#         continue
#     print(huidig_getal)

# # pizza bestellen.
# # De gebruiker voert een voor een de ingrediënten in, te kiezen uit een lijst.
# # Elk ingrediënt kan maar één keer worden besteld.
# available_toppings = ["gorgonzola", "pineapple", "ham", "bacon", "shrimp", "arugula", "mozzerella", "anchovies", "bell pepper", "pepper", "egg"]
# print(f"You can choose from the following toppings: {available_toppings}")
# toppings = []
# active = True
# while active:
#     menu = "Which topping would you like for your pizza?\n"
#     menu += "Input your toppings one by one and enter \'done\' once you're done.\n"
#     pizza_order = input(menu)
#     if pizza_order != "done":
#         if pizza_order.lower() in available_toppings and pizza_order not in toppings:
#             toppings.append(pizza_order)
#         else:
#             print("We didn\'t recognize this topping. Please check your spelling or order a different topping. Enter \'done\' once you\'re done.")
#         continue
#     else:
#         active = False
#         break
# if len(toppings) == 0:
#     print("You have ordered a pizza without any toppings.")
# elif len(toppings) == 1:
#     print("You have ordered a pizza with the following topping:")
# else:
#     print("You have ordered a pizza with the following toppings:")
# for topping in toppings:
#     print(topping.title())

# # een bepaalde waarde uit een lijst verwijderen als die vaker voorkomt
# huisdieren = ['hond', 'kat', 'kat', 'parkiet', 'hond', 'goudvis']
# while 'kat' in huisdieren:
#     huisdieren.remove('kat')
# print(huisdieren)

# # een dictionary maken met input van de gebruiker
# doorgaan = True
# huisdieren = {}
# while doorgaan:
#     name = input("Hoe heet je? ")
#     dier = input("Wat voor huisdier heb je? ")
#     huisdieren[name] = dier
#     meer_invoer = input("Wil je nog iemand toevoegen? Typ 'ja' of 'nee'. ")
#     if meer_invoer == 'nee':
#         doorgaan = False
# print(huisdieren)

# # geplaatste bestelling
# broodjes_besteld = ['ham en kaas',
#                     'sla en spek',
#                     'tomaat en mozzarella',
#                     'sla en spek',
#                     'ei',
#                     'sla en spek']
# broodjes_verwerkt = []
# nieuwe_bestelling_nodig = []

# # 'sla en spek' en 'ei' zijn op, zodat sommige bestellingen niet doorgaan
# niet_leverbaar = ('sla en spek', 'ei')

# # checken of de bestelling iets bevat uit niet_leverbaar
# # elk niet-leverbare broodje wordt in een nieuwe lijst gezet
# # voor elk broodje in deze nieuwe lijst wordt gevraagd om een alternatief
# # als het alternatief ook niet leverbaar is, wordt om nieuwe input gevraagd.
# for niet in niet_leverbaar:
#     while niet in broodjes_besteld:
#         broodjes_besteld.remove(niet)
#         nieuwe_bestelling_nodig.append(niet)
#     while nieuwe_bestelling_nodig:
#         for nieuw in nieuwe_bestelling_nodig:
#             print(f"Broodjes met {niet} zijn op. {len(nieuwe_bestelling_nodig)} broodjes met {niet} kunnen niet verwerkt worden.")
#             alternatief = input(f"Welk broodje wilt u bestellen in plaats van {niet}?\n")
#             if alternatief in niet_leverbaar:
#                 print("Dit broodje is niet voorradig.\n")
#                 break
#             broodjes_besteld.append(alternatief)
#             nieuwe_bestelling_nodig.remove(nieuw)

# # printen welke broodjes klaarliggen (of eigenlijk: de uiteindelijke bestelling)
# # nog even een overzicht van alle bestelde broodjes
# while broodjes_besteld:
#     for broodje in broodjes_besteld:
#         print(f"Er ligt een broodje met {broodje.lower()} klaar. ")
#         broodjes_besteld.remove(broodje)
#         broodjes_verwerkt.append(broodje)
# print(broodjes_verwerkt)


vakantieplannen = {}
doorgaan = True
while doorgaan == True:
    naam = input("Hoe heet je? ")
    bestemming = input("Waar wil je naartoe op vakantie? ")
    vakantieplannen[naam] = bestemming
    nog_meer = input("Wil je nog meer vakantieplannen invoeren? Typ 'ja' of 'nee'. ")
    if nog_meer == 'nee':
        doorgaan = False
print(vakantieplannen)
