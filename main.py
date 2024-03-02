import pandas as pd
import numpy as np

# Charger le fichier CSV
explorer_df = pd.read_csv("parcours_explorateurs.csv")

# Créer un dictionnaire pour représenter le graphe
graph = {}
for _, row in explorer_df.iterrows():
    if row["noeud_amont"] not in graph:
        graph[row["noeud_amont"]] = []
    graph[row["noeud_amont"]].append(row["noeud_aval"])

# Fonction récursive pour la recherche en profondeur (DFS)
def dfs(node, visited, path):
    visited.add(node)
    path.append(node)
    longest_path = []

    if node in graph:
        for neighbor in graph[node]:
            if neighbor not in visited:
                new_path = dfs(neighbor, visited, path.copy())
                if len(new_path) > len(longest_path):
                    longest_path = new_path

    return longest_path

# Recherche du chemin le plus long à partir de chaque nœud de départ
longest_path = []
for starting_node in graph.keys():
    visited = set()
    path = []
    current_longest_path = dfs(starting_node, visited, path)
    if len(current_longest_path) < len(longest_path):
        longest_path = current_longest_path

# Afficher l'explorateur avec le chemin le plus long et la longueur de ce chemin
print("L'explorateur avec le chemin le plus long est :", starting_node)
print("La longueur de son chemin est :", len(longest_path))

# initialisation des variables pour stocker l'explorateur ayant le chemin le plus court et sa longueur
explorer_with_shortest_path = None
shortest_path_length = float('inf')

# Parcourir chaque explorateur
for starting_node in graph.keys():
    current_path = [starting_node]
    current_node = starting_node

    # construction du chemin parcouru par l'explorateur
    while current_node not in array_arrival_node:
        next_node = dict_upstream_downstream[current_node]
        current_path.append(next_node)
        current_node = next_node

    # Mise à jour de l'explorateur et la longueur du chemin le plus court
    if len(current_path) < shortest_path_length:
        shortest_path_length = len(current_path)
        explorer_with_shortest_path = starting_node

print("L'explorateur avec le chemin le plus court est :", explorer_with_shortest_path)
print("La longueur de son chemin est :", shortest_path_length)


     #Calculer la longueur de chaque chemin
path_lengths = []
for starting_node in graph.keys():
    current_path = [starting_node]
    current_node = starting_node

    while current_node not in array_arrival_node:
        next_node = dict_upstream_downstream[current_node]
        current_path.append(next_node)
        current_node = next_node

    path_lengths.append(len(current_path))

# Calcul de la moyenne
mean_length = np.mean(path_lengths)

# Calcul de la médiane
median_length = np.median(path_lengths)

# Calcul de l'écart-type
std_dev_length = np.std(path_lengths)

# Calcul de l'écart interquartile
Q1 = np.percentile(path_lengths, 25)
Q3 = np.percentile(path_lengths, 75)
interquartile_range = Q3 - Q1

# Affichage des résultats
print("Moyenne de la longueur des chemins :", mean_length)
print("Médiane de la longueur des chemins :", median_length)
print("Écart-type de la longueur des chemins :", std_dev_length)
print("Écart interquartile de la longueur des chemins :", interquartile_range)

# Ajout de la boucle pour afficher les explorateurs et leurs chemins
for starting_node in graph.keys():
    current_path = [starting_node]
    current_node = starting_node
    while current_node not in array_arrival_node:
        next_node = dict_upstream_downstream[current_node]
        current_path.append(next_node)
        current_node = next_node
    print("Explorateur :", starting_node)
    print("Chemin parcouru :", current_path)
    
    
#Pour infos je l'ai fais sur notebook jupyter avec un environnement virtuelle au cas ou vous avez des problemes pou le lancer :)    
