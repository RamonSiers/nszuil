import random
from datetime import datetime

naam = input("Voer je naam in: ")
if naam == '':
    naam = 'Anoniem'
else:
    naam = naam

bericht = input("Geef hier je feedback met een max van 140 karakters: ")

if len(bericht) > 140:
    print("Voer een bericht in van max 140 karakters")
else:
    print("Bedankt voor je feedback")

datum = datetime.today()

locatielijst = ['Utrecht', 'Enschede', 'Amersfoort']
locatie = random.choice(locatielijst)

infile = open('tekstbestand zuil', 'r')
lineList = infile.readlines()
beichtnummer = 0


outfile = open('tekstbestand zuil', 'a+')
outfile.write( "\n" f"{(bericht)};{(naam)};{(datum)};{(locatie)};" )
outfile.close()