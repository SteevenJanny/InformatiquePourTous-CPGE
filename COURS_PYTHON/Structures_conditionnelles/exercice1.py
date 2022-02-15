"""
    Cours : Structures conditionnelles
    Exercice : Année bissextile
"""
an = -46

assert an >= -45, "Les annees bissextiles n'existaient pas avant!"

if an % 4 != 0:
    estBissextile = False
elif an % 400 == 0:
    estBissextile = True
elif an % 100 == 0:
    estBissextile = False
else:
    estBissextile = True

if estBissextile:
    print("l'an " + str(an) + " est bissextile")
else:
    print("l'an " + str(an) + " n'est pas bissextile")
