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
    jaar = 0
    while jaar < x:
        geld = geld * rente
        jaar +=1
        if jaar == x:
            print(f'Je spaargeld na {x} jaar is {round(geld,2)}.')

# hieronder: zelfde resultaat met ander soort loop
# voeg de if-statement van hierboven toe om alleen het laatste jaar te tonen

def spaargeld2(geld,rente,x):
    for jaar in range(0,(x+1)):
        if jaar == 0:
            geld = geld
        else:
            geld = geld * rente
        print(f'Na {jaar} jaar heb je {round(geld,2)} spaargeld.')

spaargeld(1000,1.03,5)
spaargeld2(1000,1.03,5)

# met input van de gebruiker

geld = float(input('Startinleg: '))
rentepercentage = float(input('Rentepercentage in procent: '))
jaar = float(input('Jaar: '))
rente = (100.0 + rentepercentage) / 100
huidige_spaargeld = geld * rente**jaar
print(f"Na {jaar} jaar heb je {round(huidige_spaargeld,2)} spaargeld.")
