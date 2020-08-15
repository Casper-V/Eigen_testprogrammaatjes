# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 15:48:06 2020

@author: Casper
"""

def toon_richting(richtingen):
    """"De eerste richtingaanwijzing van de route wordt apart beschreven.
    Dan komen de resterende richtingaanwijzingen.
    Tot slot een laatste aanwijzing."""
    eerste_richtingaanwijzing = route[0]
    overige_richtingaanwijzingen = route[1:-1]
    laatste_richtingaanwijzing = route[-1]
    print(f"Eerst ga je {eerste_richtingaanwijzing}.")
    for richting in overige_richtingaanwijzingen:
        print(f"Vervolgens ga je {richting}.")
    print(f"Tot slot ga ja {laatste_richtingaanwijzing}. Je hebt je bestemming bereikt.")

# Een willekeurige routebeschrijving weergegeven als lijst
# route = ['rechtdoor', 'rechtsaf', 'na 50 meter schuin naar links', 'bij het stoplicht rechtsaf', 'linksaf']


# Hieronder het alternatief waarbij de gebruiker de lijst invoert.

route =[]

eindcommando = "route klaar"
invoer_actief = True
while invoer_actief:
    aanwijzing = input(f"Typ \'{eindcommando}\' als de route klaar is of geef de volgende stap in de routebeschrijving op: ")
    if aanwijzing == eindcommando:
        invoer_actief = False
        break
    else:
        route.append(aanwijzing)

toon_richting(route)