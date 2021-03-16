# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 18:36:36 2020

@author: Casper
"""
# Een stukje code om een gastenlijst aan te leggen in een extern bestand

# het bestand dat eenmalig wordt gecreëerd met een inleidende zin
bestand = 'gastenlogboek.txt'
# with open(bestand, 'w') as gastenboek:
#     gastenboek.write("De volgende gasten hebben het hier naar hun zin gehad:\n")

# de gast vragen hoe hij/zij heet
gast = input("Hoe heet je? ")
gast = gast.title() + '\n'

# de naam van de gast wordt toegevoegd aan het gemaakte bestand
with open(bestand, 'a') as gastenboek:
    gastenboek.write(gast)
    # print(f"{gast.title()} is toegevoegd aan het gastenboek!")

# de gast kan ook namen van de rest van het gezelschap opgeven
while True:
    print("Voer de volgende naam van je gezelschap in of typ 'klaar' als je klaar bent.")
    gast = input("Hoe heet je? ")
    if gast.lower() == 'klaar':
        break
    else:
        # print(f"{gast.title()} is toegevoegd aan het gastenboek!")
        gast = gast.title() + '\n'
        with open(bestand, 'a') as gastenboek:
            gastenboek.write(gast)
