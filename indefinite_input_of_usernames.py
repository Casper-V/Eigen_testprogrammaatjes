# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 21:16:15 2020

@author: Casper
"""

credentials_dict = {}

def credentials(username,password):
    print(f"{username}\'s password is {password}.")
    credentials_dict.update({username:password})

while True:
    print("You will be asked to enter your user name and password. You can press q to quit.")
    user = input("Enter your user name: ")
    if user == "q":
        break
    passw = input("Enter your password: ")
    if passw == "q":
        break
    else:
        credentials(user,passw)
    print(credentials_dict)

