
#Fetching Data
import time
import pywapi
import pprint
import sqlite3

pp = pprint.PrettyPrinter(indent=4)
i = 1
#Verbinde zu Datenbank
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

#Drop all existing Tables
#cursor.execute("DROP TABLE Temperatures")

#Create Table
#cursor.execute(""" CREATE TABLE temperatures(origin TEXT, temp TEXT, date TEXT)""")

def getData():
	cities = pywapi.get_cities_from_google('de') # or (country = 'fr', hl = 'de')
	locidparis = pywapi.get_loc_id_from_weather_com("Paris")
	locidbs = pywapi.get_loc_id_from_weather_com("Braunschweig")
	locidlondon = pywapi.get_loc_id_from_weather_com("London")

	Bs = pywapi.get_weather_from_weather_com("GMXX0013")
	Paris = pywapi.get_weather_from_weather_com("FRXX0076")
	London = pywapi.get_weather_from_weather_com("UKXX0085")

	datetime = time.strftime("Date: %d-%B-%Y  Time: %H:%M:%S")

	tempBs = str(Bs['current_conditions']['temperature'])
	tempLondon = str(London['current_conditions']['temperature'])
	tempParis = str(Paris['current_conditions']['temperature'])

##	pp.pprint(datetime)
##	pp.pprint("Aktuelle Temperatur in Braunschweig: " + tempBs +" Grad")
##	pp.pprint("Aktuelle Temperatur in London: " + tempLondon +" Grad")
##	pp.pprint("Aktuelle Temperatur in Paris: " + tempParis +" Grad")

	werte = [('Braunschweig', tempBs, str(datetime)),
                 ('London', tempLondon, str(datetime)),
                 ('Paris', tempParis, str(datetime))]
	cursor.executemany("INSERT INTO temperatures VALUES (?,?,?)", werte)
	connection.commit()

while i<5:

	getData()
	pp.pprint("+++++++++++++++++++++++++++++++++++")
	pp.pprint("Braunschweig Data: ")
	cursor.execute(" Select * from temperatures WHERE origin = 'Braunschweig'")
	pp.pprint(cursor.fetchall())
	pp.pprint("London Data: ")
	cursor.execute(" Select * from temperatures WHERE origin = 'London'")
	pp.pprint(cursor.fetchall())
	pp.pprint("Paris Data: ")
	cursor.execute(" Select * from temperatures WHERE origin = 'Paris'")
	pp.pprint(cursor.fetchall())
	time.sleep(2800)
	#i = i +1
	
#connection.close()
