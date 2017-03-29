import activites

conn = sqlite3.connect('/hometu/etudiants/b/l/E155781C/workspace/Semestre4/Git/Python_TD2/BD/TD2_python.db');
cur = conn.cursor()

cur.execute("SELECT * FROM equipements_activites LIMIT 1 OFFSET 2")
noms2 = cur.fetchone()

print(noms2)

test = Activites(noms2)
print(vars(test))
test.toString
