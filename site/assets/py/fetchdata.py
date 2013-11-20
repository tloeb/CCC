
#Fetching Data
import time
import pywapi
import pprint
import sqlite3

pp = pprint.PrettyPrinter(indent=4)

#Verbinde zu Datenbank
connection = sqlite3.connect('temps.db')
cursor = connection.cursor()

#Drop all existing Tables
cursor.execute("DROP TABLE Temperatures")
	
def getData():
	cities = pywapi.get_cities_from_google('de') # or (country = 'fr', hl = 'de')
	locidhn = pywapi.get_loc_id_from_weather_com("Hannover")
	locidbs = pywapi.get_loc_id_from_weather_com("Braunschweig")
	locidsc = pywapi.get_loc_id_from_weather_com("London")

	tempbs = pywapi.get_weather_from_weather_com("GMXX0013")
	temphn = pywapi.get_weather_from_weather_com("GMXX0051")
	templo = pywapi.get_weather_from_weather_com("UKXX0085")
	
	datetime = time.strftime("Date: %d-%B-%Y  Time: %H:%M:%S")

	#pp.pprint(locidlo)		# London Loc ID UKXX0085
	#pp.pprint(locidbs)		# Braunschweig Loc ID: GMXX0013
	#pp.pprint(locidhn)		# Hannover Loc ID: GMXX0051

	#pp.pprint(tempbs)		
	pp.pprint(datetime)
	pp.pprint("Aktuelle Temperatur in Braunschweig: " + tempbs['current_conditions']['temperature'] +" Grad")
	pp.pprint("Aktuelle Temperatur in London: " + templo['current_conditions']['temperature'] +" Grad")
	pp.pprint("Aktuelle Temperatur in Hannover: " + temphn['current_conditions']['temperature'] +" Grad")
	
	cursor.execute(" INSERT INTO temp VALUES ('Braunschweig',?, ?)", datetime, tempbs)

	
cursor.execute(" CREATE TABLE Temperatures(origin text, time text, temp text)")
	
for i in range(0, 10):
	
	pp.pprint("+++++++++++++++++++++++++++++++++++")
	getData()
	writeData()
	cursor.execute(" SELECT * FROM Temperatures")
	time.sleep(3)

connection.commit()
connection.close()
