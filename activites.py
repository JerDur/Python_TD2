import sqlite3, csv


class Activites:
    
    noms = []
    conn = sqlite3.connect('/hometu/etudiants/b/l/E155781C/workspace/Semestre4/Git/Python_TD2/BD/TD2_python.db');
    cur = conn.cursor()
    
    def __init__(self, args):
        """Creation d'une nouvelle activite"""
        noms = self.appelConstruct()
        #On fait appel à appelConstruct pour récuperer les attributs de la base de données pour s'en servir dans le   constructeur
        for i in range(len(noms)):
            #Le setattr est une méthode permettant de créer des attributs, dans self, avec comme nom noms[i] et en tant que valeur args[i]
            setattr(self, noms[i], args[i])
        
        
    def appelConstruct(self):
        """Methode pour le constructeur qui prends la première ligne de la base de données"""
        cur.execute("SELECT * FROM equipements_activites LIMIT 1")
        attributs = [description[0] for description in cur.description]
        return attributs
        
    
    def toString(self):
        """Retourne un string de la liste des attributs avec leurs valeurs"""
        return repr(self.__dict__)