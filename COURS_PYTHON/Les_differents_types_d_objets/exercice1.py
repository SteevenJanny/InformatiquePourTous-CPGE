"""
    Cours : Les différents types d'objets
    Exercice : Un peu de géopolitique
"""

us = ["etats-unis", 210, 332, 19390]
japon = ["japon", 105, 125, 4872]
france = ["france", 51, 65, 2582]
rfa = ["allemagne de l'Ouest", 63, 84, 0]
uk = ["royaume-uni", 56, 68, 2622]
italie = ["italie", 53, 61, 1934]
canada = ["canada", 21, 38, 1653]
russie = ["russie", 130, 146]
# solution 1
G5 = [["etats-unis", 210, 332, 19390], ["japon", 105, 125, 4872], ["france", 51, 65, 2582],
      ["allemagne de l'Ouest", 63, 84, 0], ["royaume-uni", 56, 68, 2622]]
# solution 2
G5 = [us, japon, france, rfa, uk]  # Attention : dans ce cas, modifier rfa entrainera une modification de G5

# Avec des concaténations
pays = G5[0]
print(pays[0].upper() + " : population de " + str(pays[1]) + " millions d'habitants en 1970 et " + str(
    pays[2]) + " en 2020, pour un PIB de " + str(pays[3]) + " milliards USD")

# Avec un formatage
print(
    f"{pays[0].upper()} : population de {pays[1]} millions d'habitants en 1970 et {pays[2]} en 2020, pour un PIB de {pays[3]}")

for pays in G5:
    print(pays[0].upper() + " : population de " + str(pays[1]) + " millions d'habitants en 1970 et " + str(
        pays[2]) + " en 2020, pour un PIB de " + str(pays[3]) + " milliards USD")

G7 = G5.copy()
G7.append(italie)
G7.append(canada)

G7[3][0] = "allemagne"
G7[3][1] += 18
G7[3][3] = 3677

G7_by_pop = sorted(G7, key=lambda pays: pays[1])
G7_by_pop_dec = sorted(G7, key=lambda pays: pays[1], reverse=True)
G7_by_alp = sorted(G7, key=lambda pays: pays[0])

G8 = G7.copy()
G8.append(russie)
G8.pop(7)

# creation en 1974
G5_d = {"etats-unis": [210, 332, 19390], "japon": [105, 125, 4872], "france": [51, 65, 2582],
        "allemagne de l'Ouest": [63, 84, ], "royaume-uni": [56, 68, 2622]}
# ajout de l'Italie et du Canada
G7_d = dict(G5_d)
G7_d["italie"] = [53, 61, 1934]
G7_d["canada"] = [21, 38, 1653]
# alternative
G7_d.update({"italie": [53, 61, 1934], "canada": [21, 38, 1653]})
# modification du statut allemand
G7_d["allemagne"] = G7_d.pop("allemagne de l'Ouest")
G7_d["allemagne"][0] += 18
G7_d["allemagne"].append(3677)

G7_d_by_pop = sorted(G7_d.items(), key=lambda t: t[1][0])
G7_d_by_pop_dec = sorted(G7_d.items(), key=lambda t: t[1][0], reverse=True)
G7_d_by_alp = sorted(G7_d.items(), key=lambda t: t[0])

# ajout et suppression de la russie
G8_d = G7_d.copy()
G8_d["russie"] = [130, 146]
del G8_d["russie"]  # alternative a G8_d.pop("russie")

pop_tot_G8 = 0
pib_tot_G8 = 0
for key, value in G8_d.items():  # parcourt les éléments du dictionnaire
    pop_tot_G8 += value[1]  # ajoute la population en 2020
    pib_tot_G8 += value[2]  # ajoute le PIB
print("Le G7 représente {0:.2f}% de la population mondiale, et {1:.2f}% du PIB".format(pop_tot_G8 / 7800 * 100,
                                                                                       pib_tot_G8 / 81000 * 100))
