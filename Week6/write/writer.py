import csv

name =  input("What's your name? ")
home = input("Where's your home? ")

with open("writer.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])
