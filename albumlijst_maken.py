# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 21:29:18 2020

@author: Casper
"""


def make_album(artist, album_title, n_tracks=0):
    album_info = {"Artist":artist,
                  "Album title":album_title,
                  "Number of tracks":n_tracks}
    # print(album_info)

album_list = [["Bob Dylan", "Greatest Hits", 19], ["John Travolta", "Mix Tapes", 4], ["Guns N Roses", "Paradise City", 2]]
for album in album_list:
        make_album(album[0],album[1],album[2])
        
while True:
    print("Enter the artist, album title and number of tracks. You can press q to quit.")
    artist = input("Artist: ")
    if artist == "q":
        break
    album_title = input("Album title: ")
    if album_title == "q":
        break
    n_tracks = int(input("No. tracks: "))
    if n_tracks == "q":
        break
    else:
        make_album(artist, album_title,n_tracks)
        new_album_to_add = [artist, album_title, n_tracks]
    album_list.append(new_album_to_add)

print(album_list)
