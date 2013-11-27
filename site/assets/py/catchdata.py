#!/usr/bin/ python

import sqlite3
import json

#Verbinde zu Datenbank
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

cursor.execute(" Select origin,temp from temperatures")
BSData = cursor.fetchall()

print ("Content-type: application/json")
print (json.JSONEncoder().encode(BSData))



