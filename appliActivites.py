import sqlite3

try:
    import activites
except ImportError:
    print("Il faut mettre à jour le path")


conn = sqlite3.connect('/hometu/etudiants/b/l/E155781C/workspace/Semestre4/Git/Python_TD2/BD/TD2_python.db');
cur = conn.cursor()


def transform_equip():
    cur.execute("SELECT * FROM equipements_activites")
    tout = cur.fetchall()
    objets = []
    for ligne in tout:
        try:
            objets.append(Activites(ligne))
        except NameError:
            print("Le path n'a pas été mis à jour")
        except IndexError:
            print("Une erreur a eu lieu vis à vis de la liste")
    