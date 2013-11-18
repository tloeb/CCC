import sys
from argparse import ArgumentParser
from xml.dom import minidom
try:
    from urllib.request import urlopen
    from urlib.parse import urlencode
except ImportError:
    from urllib import urlopen, urlencode

API_URL = "http://www.google.com/ig/api?"

def main():
    arguments = ArgumentParser(prog="weather")
    arguments.add_argument("--unit", choices="CF", dest="unit", default="C", help="which unit to display")
    arguments.add_argument("location", nargs="+")
    args = arguments.parse_args(sys.argv[1:])

    for location in args.location:
            url = API_URL + urlencode({"weather": location})
            xml = urlopen(url).read()
            doc = minidom.parseString(xml)

            forecast_information = doc.documentElement.getElementsByTagName("forecast_information")[0]
            city = forecast_information.getElementsByTagName("city")[0].getAttribute("data")
