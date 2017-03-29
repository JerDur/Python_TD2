import sqlite3, csv, pprint


class Activites:
    
    noms = []
    commande = ""
    nbrAttr = 0
    conn = sqlite3.connect('/hometu/etudiants/b/l/E155781C/workspace/Semestre4/Git/Python_TD2/BD/TD2_python.db');
    cur = conn.cursor()
    
    def __init__(self, args):
        """Creation d'une nouvelle activite"""
        noms = self.appelConstruct
        for i in range(len(noms)):
            self.noms[i] = args[i]
            print(noms[i] + " = " + str(args[i]))
        self.t1 = 3
        
    def appelConstruct(self):
        cur.execute("SELECT * FROM equipements_activites LIMIT 1")
        ligne = [description[0] for description in cur.description]
        return ligne
        print(noms)
    
    def toString(self):
        return self.ComInsee


