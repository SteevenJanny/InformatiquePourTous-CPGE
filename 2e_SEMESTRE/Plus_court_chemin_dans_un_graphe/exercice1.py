"""
    Cours : Plus court chemin dans un graphe
    Exercice : Nombre de Bacon
"""
import numpy as np
import heapdict


def get_actor_and_film():
    """ Q1 : Après avoir analysé la structure du fichier de données, coder une fonction qui renvoie la liste des
    acteurs et celle des films (attention aux doublons); puis une autre fonction qui renvoie une matrice A telle que... """
    # On commence par extraire les lignes du fichier bacon.txt
    with open("bacon.txt", 'r') as f:
        data = f.readlines()  # Chaque ligne devient un élément de la liste data

    # On découpe chaque ligne par le symbole '/', et on ne garde que le premier élément.
    list_film = [ligne.split('/')[0] for ligne in data]

    list_actor = []
    for ligne in data:
        movie_actors = ligne.split('/')[1:]  # Découpe la ligne, et retire le titre du film
        movie_actors[-1] = movie_actors[-1][:-1]  # Retire \n en fin de ligne
        for actor in movie_actors:
            if actor not in list_actor:  # On vérifie que l'acteur n'est pas déjà dans la liste
                list_actor.append(actor)
    return list_film, list_actor


def get_adjacency_matrix(list_film, list_actor):
    with open("bacon.txt", 'r') as f:
        data = f.readlines()  # Chaque ligne devient un élement de la liste data

    # Initialisation de la matrice
    adjacency_matrix = [[None for _ in range(len(list_actor))] for _ in range(len(list_actor))]

    for ligne in data:  # Pour chaque film
        movie_actors = ligne.split('/')[1:]  # On récupère le nom des acteurs
        movie_actors[-1] = movie_actors[-1][:-1]  # Retire \n
        movie_name = ligne.split('/')[0]  # nom du film

        idx_movie = list_film.index(movie_name)  # indice du film
        for actor1 in movie_actors:
            for actor2 in movie_actors:
                idx_actor1 = list_actor.index(actor1)  # indice de l'acteur 1
                idx_actor2 = list_actor.index(actor2)  # indice de l'acteur 2
                # La matrice est symétrique
                adjacency_matrix[idx_actor1][idx_actor2] = idx_movie
                adjacency_matrix[idx_actor2][idx_actor1] = idx_movie
    return adjacency_matrix


def dijkstra(adjacency_matrix, list_actor):
    """ Q2 : Coder l'algorithme de Dijkstra pour calculer la distance entre Kevin Bacon et tous les acteurs du fichier
    de données."""
    distances = [np.inf] * len(adjacency_matrix)  # Matrice des distances

    idx_kevin_bacon = list_actor.index("Kevin Bacon")  # noeud de départ : KB
    distances[idx_kevin_bacon] = 0  # Distance de KB à lui-même

    P = heapdict.heapdict()  # Initialise la file de priorité
    C = {}  # Initialise la liste des provenances sous forme de dictionnaire
    P[idx_kevin_bacon] = 0  # Ajout du premier sommet dans la file

    while len(P) > 0:
        V = P.popitem()[0]  # Récupère le noeud de plus petite distance dans la file
        # Calcul des voisins
        voisins = [i for i in range(len(list_actor)) if adjacency_matrix[i][V] is not None]

        for v_i in voisins:
            new_distance = distances[V] + 1  # Distance + 1 film
            if distances[v_i] > new_distance:
                C[v_i] = V
                distances[v_i] = new_distance
                P[v_i] = new_distance
    return C


def get_path_to(actor, list_actor, provenance, list_film, adjacency_matrix):
    """ Q3 : Afficher le chemin entre Morgan Freeman et Kevin Bacon sous la forme d'une série de lignes : 
    x a joué dans f avec y
    De la même manière, afficher celui entre Brigitte Bardot et Kevin Bacon."""
    idx_bacon = list_actor.index('Kevin Bacon')  # index de KB
    current_idx = list_actor.index(actor)  # index de l'acteur

    while current_idx != idx_bacon:
        next_idx = provenance[current_idx]  # Acteur suivant dans la liste de provenance
        film = list_film[adjacency_matrix[current_idx][next_idx]]  # nom du film qui fait le lien

        print(list_actor[current_idx], 'a joué dans ', film, " avec ", list_actor[next_idx])

        current_idx = next_idx


def get_bacon_number(list_actor, provenance):
    """ Q4 : Calculer les nombres de Bacon de tous les acteurs de la liste."""
    bacon_numbers = []
    idx_bacon = list_actor.index('Kevin Bacon')  # index de KB
    for idx in range(len(list_actor)):
        bacon_numbers.append(0)  # Initialise le nombre de Bacon à zéro
        current_idx = idx
        while current_idx != idx_bacon:
            next_idx = provenance[current_idx]
            current_idx = next_idx
            bacon_numbers[-1] += 1  # Mise à jour du nombre de Bacon
    return bacon_numbers


if __name__ == '__main__':
    list_film, list_actor = get_actor_and_film()
    adjacency_matrix = get_adjacency_matrix(list_film, list_actor)
    C = dijkstra(adjacency_matrix, list_actor)
    print(get_path_to('Morgan Freeman', list_actor, C, list_film, adjacency_matrix))
    print(get_path_to('Brigitte Bardot', list_actor, C, list_film, adjacency_matrix))

    bacon_numbers = get_bacon_number(list_actor, C)
    bacon_max = max(bacon_numbers)

    print([actor for i, actor in enumerate(list_actor) if bacon_numbers[i] == bacon_max], bacon_max)
    print("Nombre de Bacon moyen : ", np.mean(bacon_numbers))
