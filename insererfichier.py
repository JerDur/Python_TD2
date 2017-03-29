import sqlite3
import csv

conn = sqlite3.connect('/hometu/etudiants/d/u/E155781C/Semestre4/Git/Python_TD2/BD/TD2_python.db');

cur = conn.cursor()

def fonction(test):
    liste = []
    attributs = []
    attributs2 = []
    attributs3 = []
    
    for row in test:
        liste.append(row)
        break
    for x in liste:
        for y in x:
            attributs.append(y)
            
    #print(attributs)
    for x in attributs:
        a = x.replace(" ","")
        b = a.replace("'","")
        attributs2.append(b)
    
    for z in attributs2:
        if(z[0]!='"'):
            a = z + ' Integer'
            attributs3.append(a)
        else:
            a = z[1:-1] + ' text'
            attributs3.append(a)
    #print(attributs2)
    #print(attributs2[0])
    

    b = ''
    print(b)
    for x in attributs3:
        b += (x + ', ')
    b = b[:-2]
    return b

#conn.execute("CREATE TABLE equipements_activites(ComInsee double,ComLib text,EquipementId double,EquNbEquIdentique double,ActCode double,ActLib text,EquActivitePraticable text,EquActivitePratique text,EquActiviteSalleSpe text,ActNivLib text)")
#conn.execute("CREATE TABLE installations_table(NomInstallation text, NumInstallation text, NomCommune text, CodeINSEE text, CodePostal text, NomLieuDit text, NumeroVoie text, NomVoie text,location text, Longitude text, Latitude text, AucunAmenagementAccessibilite text, AccessibiliteHandicapesMobiliteReduite text, AccessibiliteHandicapesSensoriels text, EmpriseFonciere text, LogementGardien text, MultiCommune text, NbrTotalParking text, NbrTotalParkingHandicapes text, InstallationParticuliere text, DesserteMetro text, DesserteBus text, DesserteTram text,DesserteTrain text, DesserteBateau text, DesserteAutre text, NombreTotalEquipementsSportifs text, NombreTotalFichesEquipements text, DateMajFicheInstallation text)")

#conn.execute("DROP TABLE equipements_activites")
#conn.execute("DROP TABLE installations_table")

with open('/hometu/etudiants/b/l/E155245U/Semestre4/Git/Python_TD2/CSV/J334_equipements_activites.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='*')
    a = fonction(reader)
    #conn.execute("CREATE TABLE equipements_activites(" + a + ")")
    print("a")
    print(a)  
    #cur.execute("INSERT INTO equipements_activites VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
     

with open('/hometu/etudiants/d/u/E155245U/Semestre4/Git/Python_TD2/CSV/23440003400026_J335_installations_table.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='*')
    c = fonction(reader)
    print("c")
    print(c)
    #conn.execute("CREATE TABLE installations_tables(" + b + ")")
        
    #cur.execute("INSERT INTO installations_table VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28]))
    
conn.commit()

conn.close()