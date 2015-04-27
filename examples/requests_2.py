import requests

url = 'http://python.org/'

# GET example

r = requests.get(url)
html = r.text

# POST example

payload = {'Nombre': 'Ariel', 'Apellido': 'Rios'}
r = requests.post(url, data=payload)  # basta de encodear :P
json = r.json()

# Y soporta todos los métodos REST
# request.put()
# requests.delete()
