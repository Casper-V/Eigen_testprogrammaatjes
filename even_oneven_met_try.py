# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 16:42:47 2020

@author: Casper
"""

import numpy as np
import pandas as pd


#1 Eerste vraag: twee cijfers invoeren

ondergrens = 10
bovengrens = 11

try:
    ondergrens = int(input('In een lijst van twintig cijfers kijken we of het cijfer even of oneven is. Ook kijken we of het cijfer binnen het bereik valt dat je invoert.\n\nVoer een cijfer in tussen 1 en 10 voor de ondergrens van de lijst: '))
    bovengrens = int(input('Voer een cijfer in tussen 11 en 20 voor de bovengrens van de lijst: '))
    print(ondergrens/bovengrens)
except ValueError:
    print('\n***Foute invoer! Geeft niks. We doen gewoon alsof je 10 en 11 hebt ingevoerd.***')

if ondergrens > 10:
    ondergrens = 10
    print('\nDe gekozen ondergrens is te hoog! Als ondergrens wordt 10 ingesteld.')
if ondergrens < 1:
    ondergrens = 1
    print('\nDe gekozen ondergrens is te laag! Als ondergrens wordt 1 ingesteld.')
if bovengrens > 20:
    bovengrens = 20
    print('\nDe gekozen bovengrens is te hoog! Als bovengrens wordt 20 ingesteld.')
if bovengrens < 11:
    bovengrens = 11
    print('\nDe gekozen bovengrens is te laag! Als bovengrens wordt 11 ingesteld.')

print('\nDit is het bereik dat we gaan controleren: ',ondergrens,'tot en met',bovengrens)

bovengrens = bovengrens + 1
bereik = range(ondergrens,bovengrens)
print('-------------------')
print('Hier zie je welke cijfers binnen dit bereik vallen:')
print('-------------------')

cijfer = 0

while cijfer < 20:
    cijfer = cijfer + 1
    if cijfer % 2 and cijfer in bereik:
        print(cijfer,'is een oneven getal en valt binnen het gekozen bereik')
    elif cijfer % 2 and not cijfer in bereik:
        print(cijfer,'is een oneven getal en valt NIET binnen het gekozen bereik')
    else:
        if cijfer in bereik:
            print(cijfer,'is een even getal en valt binnen het gekozen bereik')
        else:
            print(cijfer,'is een even getal en valt NIET binnen het gekozen bereik')

#2 Tweede vraag: één cijfer uitkiezen

gekozen_cijfer = 1

try:
    gekozen_cijfer = int(input('Deze lijst is wel wat lang, vind je ook niet? Kies één van de cijfers in de lijst om alleen dat cijfer te tonen: '))
    while gekozen_cijfer < 1 or gekozen_cijfer > 20:
        gekozen_cijfer = int(input('Je moet wel een cijfer uit de lijst kiezen. Kies een nieuw cijfer: '))
except ValueError: 
    print('\n***Foute invoer! Geeft niks. We doen gewoon alsof je 1 hebt ingevoerd.***')

if gekozen_cijfer % 2 and cijfer in bereik:
    print('\nGoede keus!',gekozen_cijfer,'is een oneven getal en valt binnen het gekozen bereik')
elif cijfer % 2 and not cijfer in bereik:
    print('\nGoede keus!',gekozen_cijfer,'is een oneven getal en valt NIET binnen het gekozen bereik')
else:
    if gekozen_cijfer in bereik:
        print('\nGoede keus!',gekozen_cijfer,'is een even getal en valt binnen het gekozen bereik')
    else:
        print('\nGoede keus!',gekozen_cijfer,'is een even getal en valt NIET binnen het gekozen bereik')

#3 Derde vraag: wil je de tabel zien of stoppen?

tabel = pd.DataFrame({'Oneven':{'a':1,'b':3,'c':5,'d':7,'e':9,'f':11,'g':13,'h':15,'i':17,'j':19},'Even':{'a':2,'b':4,'c':6,'d':8,'e':10,'f':12,'g':14,'h':16,'i':18,'j':20}})

leuk = input(str('De twintig cijfers gaan we in een tabel zetten. Ben je benieuwd hoe dat eruit ziet?\nTyp ja of nee: '))
while leuk != 'ja' and leuk != 'nee':
    leuk = input(str('Bedoelde je ja of nee? '))
if leuk == 'nee':
    print('\nJammer! Je bent aan het einde gekomen.')
    import sys
    sys.exit()
else:
    print('\nLeuk! De tabel ziet er als volgt uit:\n')
    print(tabel)

#4 Vierde vraag: vermenigvuldiging invoeren

vermenigvuldig = 2.0

try:
    vermenigvuldig = float(input('Nu gaan we de waarden vermenigvuldigen. Voer een getal in. Cijfers achter de komma zijn toegestaan, maar schrijf de komma dan als een punt! '))
    verm_string = str(vermenigvuldig)
    print('\nNu vermenigvuldigen we de waarden in de tabel met',verm_string+':\n')
except ValueError:
    print('\n***Foute invoer! Geeft niks. We doen gewoon alsof je 2.0 hebt ingevoerd.***\n')

resultaat = tabel.mul(vermenigvuldig)
resultaat.columns = ['Dit was oneven','Dit was even']
resultaat.loc['e'] = [22.0,25.0]
print(resultaat)

# Vijfde vraag: in welke rij kloppen de getallen niet?

foute_rij = str(input('\nBij één rij klopt het resultaat niet. Welke letter heeft deze rij? '))
while foute_rij != 'e':
    foute_rij = str(input('Fout! Probeer het opnieuw. Welke rij klopt niet? '))
print('Correct! Rij e klopt niet.')


print('\nHopelijk vond je dit leuk om te doen! Tot de volgende keer!' )
