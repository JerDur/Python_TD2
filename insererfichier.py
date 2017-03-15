import sqlite3
import csv

conn = sqlite3.connect('/hometu/etudiants/b/l/E155781C/workspace/Semestre4/Git/Python_TD2/BD/TD2_python.db');

cur = conn.cursor()

liste = []

#conn.execute("CREATE TABLE equipements_activites(ComInsee double,ComLib text,EquipementId double,EquNbEquIdentique double,ActCode double,ActLib text,EquActivitePraticable text,EquActivitePratique text,EquActiviteSalleSpe text,ActNivLib text)")


with open('/hometu/etudiants/b/l/E155781C/workspace/Semestre4/Git/Python_TD2/CSV/J334_equipements_activites.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='*')
    for row in reader:
        liste.append(row)

        params = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])

        
        cur.execute("INSERT INTO equipements_activites VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
    
conn.commit()

conn.close()