import sqlite3

#Verbinde zu Datenbank
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

catchData()

def catchData():
    cursor.execute(" Select temp from temperatures WHERE origin = 'Braunschweig'")
    BSData = cursor.fetchall()

    return BSData
