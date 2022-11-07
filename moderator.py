# moderator moet inloggen met email en id en dit wordt gecontroleerd met een bestand met de accountgegevens
# lees alle berichten in
# per bericht uit tekstbestand zuil kunnen beoordelen
#    deze goed of afkeuren
#    de wijziggen en tijd van beoordingen opslaan in database
# beoordeelde berichten verwijderen uit bestand
import uuid
import psycopg2
from datetime import datetime


Identificatie = 0
line = ''
email = ''
infile = open('mod.txt', 'r')
lineList = infile.readlines()
while True:
    try:
        email = input("Wat is je e-mail?: ")
    except ValueError:
        print("Voer een geldig e-mail")
    else:
        break
id = int(input('Voer je id in: '))

for line in lineList:
    if (str(email) + ';' + str(id) + '\n') == line:
        Identificatie = 1
        break

if Identificatie == 1:
    print('Je kunt gaan beoordelen')
else:
    print('De id is fout')

infile = open("tekstbestand zuil", "r")
lineList = infile.readlines()

for line in lineList:
    beoordeling = input(('(Beoordeel dit bericht met een g(goedgekeurd) of met een a(afgekeurd)'f"{(line)}: "))
    info = line.split(';')
    tekst_bericht = info[0]
    naam = info[1]
    datum_bericht = info[2]
    locatie = info[3]
    berichtnummer = uuid.uuid4()
    datum_beoordeling = datetime.today()

    connection_string = "host='localhost' dbname='Databese Zuil' user='postgres' password='kaas'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    query = f""" INSERT INTO bericht(berichtnummer, tekst_bericht, datum_bericht, id_moderator, mail_moderator, status_beoordeling, datum_beoordeling, naam_reiziger, fk_station_city)
    VALUES ('{(berichtnummer)}', '{(tekst_bericht)}', '{(datum_bericht)}', '{(id)}', '{(email)}', '{(beoordeling)}', '{(datum_beoordeling)}', '{(naam)}', '{(locatie)}') """

    cursor.execute(query)
    conn.commit()
    conn.close()

