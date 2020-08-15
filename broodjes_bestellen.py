# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 18:59:09 2020

@author: Casper
"""


# geplaatste bestelling
broodjes_besteld = ['ham en kaas',
                    'sla en spek',
                    'tomaat en mozzarella',
                    'sla en spek',
                    'ei',
                    'sla en spek']
broodjes_verwerkt = []
nieuwe_bestelling_nodig = []

# 'sla en spek' en 'ei' zijn op, zodat sommige bestellingen niet doorgaan
niet_leverbaar = ('sla en spek', 'ei')

# checken of de bestelling iets bevat uit niet_leverbaar
# elke bestelling van een niet-leverbare broodje wordt in een nieuwe lijst gezet
# voor elk broodje in deze nieuwe lijst wordt gevraagd om een alternatief
# als het alternatief ook niet leverbaar is, wordt om nieuwe input gevraagd
# de break voorkomt dat het foute broodje alsnog wordt toegevoegd
for niet in niet_leverbaar:
    while niet in broodjes_besteld:
        broodjes_besteld.remove(niet)
        nieuwe_bestelling_nodig.append(niet)
    while nieuwe_bestelling_nodig:
        for nieuw in nieuwe_bestelling_nodig:
            print(f"Broodjes met {niet} zijn op. {len(nieuwe_bestelling_nodig)} broodjes met {niet} kunnen niet verwerkt worden.")
            alternatief = input(f"Welk broodje wilt u bestellen in plaats van {niet}?\n")
            if alternatief in niet_leverbaar:
                print("Dit broodje is niet voorradig.\n")
                break
            broodjes_besteld.append(alternatief)
            nieuwe_bestelling_nodig.remove(nieuw)

# printen welke broodjes klaarliggen (of eigenlijk: de uiteindelijke bestelling)
# nog even een overzicht van alle bestelde broodjes
while broodjes_besteld:
    for broodje in broodjes_besteld:
        print(f"Er ligt een broodje met {broodje.lower()} klaar. ")
        broodjes_besteld.remove(broodje)
        broodjes_verwerkt.append(broodje)
print(broodjes_verwerkt)