#!/usr/bin/python
import urllib2, json, io

# Site here, API key at end
site = "https://openexchangerates.org/api/latest.json?app_id="

# Setting up the request handlers. This is mostly a vestige from having to spoof the headers in previous iterations as a scraper
request = urllib2.Request(site)
opener = urllib2.build_opener()

# Storing the output of the site in the html variable
json_data = opener.open(request).read()
data = json.loads(json_data)

# currencies.json is the translation table
currency_names = json.load(open('currencies.json', 'r'))

# writing out the currency information to currency.dat
with open('currency.dat', 'w') as currencydat:
        for currency in sorted(currency_names):
                # this is the currency format the backend system uses
                currencydat.write("%s %s %s %s\n" %(currency.encode('utf-8'), currency_names[currency].encode('utf-8'), 1/data['rates'][currency], data['rates'][currency]))
