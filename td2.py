import sqlite3, csv

conn = sqlite3.connect('TD2_python.db')
c = conn.cursor()
#c.execute('''CREATE TABLE stocks(date text, trans text, symbol text, qty real, price real)''')
#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
#t = ('RHAT',)
#c.execute('SELECT * FROM stocks WHERE symbol=?', t)
#c.execute('''CREATE TABLE equipements_activites(ComInsee,"ComLib",EquipementId,EquNbEquIdentique,ActCode,"ActLib","EquActivitePraticable","EquActivitePratique","EquActiviteSalleSpe","ActNivLib")''')

#f = file("J334_equipements_activites.csv", "w")
with open("Semestre4/Python/TD2/J334_equipements_activites.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    ma_liste = list(reader)
    
#print(ma_liste)
