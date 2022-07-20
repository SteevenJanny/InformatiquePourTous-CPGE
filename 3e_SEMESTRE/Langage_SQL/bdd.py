import sqlite3

c = sqlite3.connect('voyages_affaires.db')
curseur = c.cursor()

def requete(R):
	""" R est la requête écrite en syntaxe SQL, qu'il conviendra d'encadrer par une paire de triples guillemets """
	curseur.execute(R)
	for ligne in curseur:
		print(str(ligne)[1:-1])

###################### INSEREZ VOS REQUETES ICI ######################

# exemple : pour afficher les noms et prénoms de tous les employés de l'entreprise
requete(""" 
SELECT nom, prenom
FROM Employe
""")


########################## FIN DES REQUÊTES ##########################

c.commit()
c.close()