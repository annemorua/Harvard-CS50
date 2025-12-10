import json
import requests
import sys

#Extracts the JSON data.
datos = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

#If the argument does not have two words, the program ends.
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

#Checks that the second word of the argument is a number.
try:
    bitcoin = float(sys.argv[1])

#If not, the program ends.
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    #Visually sort the JSON data.
    data = datos.json()

    # Looks for how much a bitcoin is worth in dollars.
    price = data["bpi"]["USD"]["rate_float"]

except requests.RequestException:
    pass

#Multiply the number of bitcoins by its value to get the total amount and prints it.
amount = bitcoin * price

print(f"${amount:,.4f}")
