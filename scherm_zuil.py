from tkinter import *
import psycopg2
import requests
import json

connection_string = "host='localhost' dbname='Databese Zuil' user='postgres' password='kaas'"
conn = psycopg2.connect(connection_string)
cursor = conn.cursor()
query = """SELECT  tekst_bericht, naam_reiziger
        FROM bericht
        WHERE status_beoordeling = 'g' ;"""
cursor.execute(query)
records = cursor.fetchall()             # retrieve the records from the database
conn.close()
tekstblok = ''
for record in records:
    tekstblok = tekstblok + record[0] + ': ' + record[1] + '\n'


locatiestation = str(input("Wat is de locatie van het station? Amersfoort, Enschede of Utrecht, typ hier de locatie: "))

connection_string = "host='localhost' dbname='Databese Zuil' user='postgres' password='kaas'"
conn = psycopg2.connect(connection_string)
cursor = conn.cursor()
query = f"""SELECT  faciliteit_soort
        FROM faciliteit_soort
        WHERE fk_station_city = '{locatiestation}' ;"""
cursor.execute(query)
records = cursor.fetchall()             # retrieve the records from the database
conn.close()

faciliteiten = ''
for record in records:
    faciliteiten = faciliteiten + locatiestation + ':' + record[0] + '\n'


api_key = "9db0e8ba7a426ccc993e2cd352675c65"
lat = "52.1092717"
lon = "5.1809676"
url = "http://api.openweathermap.org/data/2.5/weather?appid=9db0e8ba7a426ccc993e2cd352675c65&q=Utrecht&units=metric&lang=nl"

response = requests.get(url)
data = json.loads(response.text)
print(data)

print("De Temperatuur is",data["main"]["temp"],"graden")

temperatuur = ("De Temperatuur is " + str(data["main"]["temp"]) + " graden")
print(temperatuur)

root = Tk()

img = PhotoImage(file='WeeDenseArabianwildcat-size_restricted.gif')
label = Label(master=root,
              image=img,
              background='yellow',
              foreground='blue')
label.pack()

label = Label(master=root,
              background='yellow',
              foreground='blue',
              text=f"{(tekstblok)} \n \n {(faciliteiten)} \n \n {(temperatuur)}")
label.pack()



root.mainloop()


