#!/usr/bin/ python

import sqlite3
import json

#Verbinde zu Datenbank
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

cursor.execute(" Select temp from temperatures WHERE origin = 'Braunschweig'")
BSData = cursor.fetchall()
output = "Hello"

return HttpResponse(output, content_type="application/json")



