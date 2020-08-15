# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 19:23:47 2020

@author: Casper
"""


vakantieplannen = {}
doorgaan = True
while doorgaan:
    naam = input("Hoe heet je? ")
    bestemming = input("Waar wil je naartoe op vakantie? ")
    vakantieplannen[naam] = bestemming
    nog_meer = input("Wil je nog meer vakantieplannen invoeren? Typ 'ja' of 'nee'. ")
    if nog_meer == 'nee':
        doorgaan = False
print(vakantieplannen)
for naam, bestemming in vakantieplannen.items():
    print(f"{naam} wil op vakantie naar {bestemming}.")