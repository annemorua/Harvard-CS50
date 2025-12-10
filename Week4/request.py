#Los AIPs se pueden obtener de la dirección docs.python-requests.org.
#Son files y functions de terceros que se conectan al server de esa AIP.
import json
#Este no se tiene que installar por medio de pip.
import requests
import sys

#Se va a trabajar con "iTunes".

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

#Este imprime el monton de letras y valores.
print(response.json())

#Este hace que sea un poco más fácil leerlo.
#print(json.dumps(response.json(), indent=2))

#Cuando se "imprime" aparecen la cantidad de canciones que yo le haya puesto en el límite del "https....

o = response.json()
for result in o["results"]:
    print(result["trackName"])

#Para usar JSON se puede visitar la dirección docs.python.org/3/library/json.html.
