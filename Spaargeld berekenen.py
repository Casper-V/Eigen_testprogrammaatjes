# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 17:18:41 2020

@author: Casper
"""

# programma om het spaargeld te berekenen na x jaar
# startgeld = 1000
# rente = 1.03 (d.w.z. 3%)
# x = 5

def spaargeld(geld,rente,x):
    """berekent spaargeld na x jaar met een while-loop"""
    jaar = 0
    while jaar < x:
        geld = geld * rente
        jaar +=1
        if jaar == x:
            print(f'Je spaargeld na {x} jaar is {round(geld,2)}.')

# hieronder: zelfde resultaat met ander soort loop
# voeg de if-statement van hierboven toe om alleen het laatste jaar te tonen

def spaargeld2(geld,rente,x):
    """berekent spaargeld na x jaar met een for-loop
        inclusief alle tussenliggende jaren"""
    for jaar in range(0,(x+1)):
        if jaar == 0:
            geld = geld
        else:
            geld = geld * rente
        print(f'Na {jaar} jaar heb je {round(geld,2)} spaargeld.')

spaargeld(1000,1.03,5)
spaargeld2(1000,1.03,5)

# met input van de gebruiker

geld_input = float(input('Startinleg: '))
rentepercentage_input = float(input('Rentepercentage in procent: '))
x_input = float(input('Jaar: '))
rente_input = (100.0 + rentepercentage_input) / 100
# de onderstaande twee regels kunnen evt. de function call vervangen
# huidige_spaargeld = geld * rente**jaar
# print(f"Na {jaar} jaar heb je {round(huidige_spaargeld,2)} spaargeld.")
spaargeld(geld_input, rente_input, x_input)
