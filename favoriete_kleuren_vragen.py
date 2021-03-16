# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 19:02:09 2020

@author: Casper
"""
# Een loop om favoriete kleuren van mensen toe te voegen aan een nieuw, leeg tekstbestand.
# Eventueel kun je starten met een lege lijst en daar de antwoorden aan toevoegen.
# Dan kun je met een for-loop door de lijst lopen en de antwoorden een voor een appenden aan het tekstbestand.
while True:
    print("Typ 'stop' om te stoppen.")
    kleur = input("Wat is je favoriete kleur? ")
    kleur = kleur.lower()
    if kleur == 'stop':
        break
    else:
        with open('favoriete_kleuren_enquete.txt', 'a') as favo_kleuren:
            favo_kleuren.write(kleur + '\n')
