import sqlite3
import csv

conn = sqlite3.connect('/hometu/etudiants/d/u/E155245U/Semestre4/Git/Python_TD2/BD/TD2_python.db');

cur = conn.cursor()

liste = []

#conn.execute("CREATE TABLE equipements_activites(ComInsee double,ComLib text,EquipementId double,EquNbEquIdentique double,ActCode double,ActLib text,EquActivitePraticable text,EquActivitePratique text,EquActiviteSalleSpe text,ActNivLib text)")
#conn.execute("CREATE TABLE installations_table(NomInstallation text, NumInstallation text, NomCommune text, CodeINSEE text, CodePostal text, NomLieuDit text, NumeroVoie text, NomVoie text,location text, Longitude text, Latitude text, AucunAmenagementAccessibilite text, AccessibiliteHandicapesMobiliteReduite text, AccessibiliteHandicapesSensoriels text, EmpriseFonciere text, LogementGardien text, MultiCommune text, NbrTotalParking text, NbrTotalParkingHandicapes text, InstallationParticuliere text, DesserteMetro text, DesserteBus text, DesserteTram text,DesserteTrain text, DesserteBateau text, DesserteAutre text, NombreTotalEquipementsSportifs text, NombreTotalFichesEquipements text, DateMajFicheInstallation text)")

with open('/hometu/etudiants/d/u/E155245U/Semestre4/Git/Python_TD2/CSV/J334_equipements_activites.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='*')
    for row in reader:
        liste.append(row)
        print(liste[0])


with open('/hometu/etudiants/d/u/E155245U/Semestre4/Git/Python_TD2/CSV/J334_equipements_activites.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='*')
    for row in reader:
        liste.append(row)
        
        cur.execute("INSERT INTO equipements_activites VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))

with open('/hometu/etudiants/d/u/E155245U/Semestre4/Git/Python_TD2/CSV/23440003400026_J335_installations_table.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='*')
    for row in reader:
        liste.append(row)
        
        cur.execute("INSERT INTO installations_table VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28]))
    
conn.commit()

conn.close()