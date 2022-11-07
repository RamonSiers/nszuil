import psycopg2
connection_string = "host='localhost' dbname='Databese Zuil' user='postgres' password='kaas'"
conn = psycopg2.connect(connection_string)
cursor = conn.cursor()
query = """SELECT  tekst_bericht, naam_reiziger
        FROM bericht
        WHERE status_beoordeling = 'g' ;"""
cursor.execute(query)
records = cursor.fetchall()             # retrieve the records from the database
conn.close()
for record in records:
        print(record[0])
