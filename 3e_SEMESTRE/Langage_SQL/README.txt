Les exercices du chapitre "Langage SQL" requièrent l'utilisation d'une base de données de voyages d'affaires, qui a été présentée et utilisée tout au long du cours. Pour la récupérer, vous pouvez télécharger le fichier voyages_affaires.db.

Nous vous proposons de manipuler cette base de données via la bibliothèque sqlite3 de Python. La structure du code à utiliser est disponible dans le fichier bdd.py. 

Quelques addendums:

- Une erreur s'est malheureusement glissée dans la correction de la question 3: il faut remplacer "nom" par "E.nom" pour résoudre toute ambiguïté avec l'attribut "nom" de la table "Logement".

- La manipulation de dates n'est pas au programme: pour ne pas alourdir davantage un chapitre déjà assez consistant, nous avons écrit simplement "fin-debut" pour calculer la durée d'un séjour à l'aide des dates de fin et de début. En réalité, il faut d'abord convertir chaque date en jour julien (i.e. le nombre de jours écoulés depuis le 24 novembre 4713 av. JC midi, qui marque le début du calendrier julien). Autrement dit, au lieu d'écrire "fin-debut", il faut écrire "julianday(fin)-julianday(debut)".

- Pour votre curiosité, le code qui a servi à créer cette base de données se trouve dans le fichier creation_bdd.py. La création et la modification de bases de données n'est pas au programme.





