"""
    Cours : Manipulation de fichiers
    Exercice : Analyse de textes
"""
import csv
import matplotlib.pyplot as plt

GISTEMP = []
GCAG = []
DATE = []

# Q1 : Lire le fichier CSV, et extraire les données de chaque organisme dans deux listes différentes. Sauvegarder
# également les dates correspondantes dans une liste supplémentaire.
with open("temperature.csv", 'r') as f:
    csv_reader = csv.reader(f, delimiter=",")  # Transformation en objet CSV
    for idx_ligne, ligne in enumerate(csv_reader):
        if idx_ligne == 0:
            print(ligne)  # Affiche le nom des colonnes
        else:  # Extraction donnée
            organisme = ligne[0]
            date = int(ligne[1])  # On convertit la date en entier
            anomalie = float(ligne[2])  # Et l'anomalie en flottant

            # On stocke dans la bonne liste
            if organisme == "GISTEMP":
                GISTEMP.append(anomalie)
                DATE.append(date)
            else:
                GCAG.append(anomalie)

# Q2 : Afficher avec matplotlib l'évolution annuelle des anomalies de température selon chaque organisme

plt.grid()

plt.plot(DATE, GCAG, c="gray")
plt.plot(DATE, GISTEMP, '--', c="black")
plt.legend(["GCAG", "GCAG"])
plt.title("Evolution des valeurs moyennes des anomalies \n de température de 1880 à 2016")
plt.show()

# Q3 : Après avoir calculé la moyenne des mesures des deux organismes pour chaque année, enregistrer le résultat dans un
# nouveau fichier CSV.
moyenne = []
for i in range(len(GISTEMP)):
    moyenne.append((GISTEMP[i] + GCAG[i]) / 2)

with open("moyenne_anomalies.csv", 'w') as f:
    csv_writer = csv.writer(f, delimiter=",")  # Création d'un writer
    csv_writer.writerow(["Date", "Anomalie Moyenne"])  # Nom des colonnes

    for i in range(len(moyenne)):
        csv_writer.writerow([DATE[i], moyenne[i]])
