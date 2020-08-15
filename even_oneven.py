# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 16:42:47 2020

@author: Casper
"""


ondergrens = int(input('In een lijst van twintig cijfers kijken we of het cijfer even of oneven is. Ook kijken we of het cijfer binnen het bereik valt dat je invoert.\n\nVoer een cijfer in tussen 1 en 10 voor de ondergrens van de lijst: '))
bovengrens = int(input('Voer een cijfer in tussen 11 en 20 voor de bovengrens van de lijst: '))

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

gekozen_cijfer = int(input('Deze lijst is wel wat lang, vind je ook niet? Kies één van de cijfers in de lijst om alleen dat cijfer te tonen: '))
while gekozen_cijfer < 1 or gekozen_cijfer > 20:
    gekozen_cijfer = int(input('Je moet wel een cijfer uit de lijst kiezen. Kies een nieuw cijfer: '))

if gekozen_cijfer % 2 and cijfer in bereik:
    print('\nGoede keus!',gekozen_cijfer,'is een oneven getal en valt binnen het gekozen bereik')
elif cijfer % 2 and not cijfer in bereik:
    print('\nGoede keus!',gekozen_cijfer,'is een oneven getal en valt NIET binnen het gekozen bereik')
else:
    if gekozen_cijfer in bereik:
        print('\nGoede keus!',gekozen_cijfer,'is een even getal en valt binnen het gekozen bereik')
    else:
        print('\nGoede keus!',gekozen_cijfer,'is een even getal en valt NIET binnen het gekozen bereik')