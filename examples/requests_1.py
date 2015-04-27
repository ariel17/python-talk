url = 'http://python.org/'

# GET example

from urllib2 import urlopen

r = urlopen(url)
html = r.read()

# POST example

from urllib import urlencode
import json

data = {'Nombre': 'Ariel', 'Apellido': 'Rios'}
r = urlopen(url, urlencode(data))
json_raw = r.read()
json_obj = json.loads(json_raw)
