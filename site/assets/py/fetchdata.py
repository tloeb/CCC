import pywapi
import pprint
pp = pprint.PrettyPrinter(indent=4)

cities = pywapi.get_cities_from_google('de') # or (country = 'fr', hl = 'de')

pp.pprint(cities)