# Liste des sommets
v = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Liste des arêtes du graphe (non orienté)
e = [[1, 2], [1, 4], [4, 7], [4, 5], [7, 8],
     [2, 3], [2, 5], [5, 6], [5, 8], [8, 9], [9, 6], [6, 3]]

# Fonction pour trouver les voisins d'un sommet donné dans un graphe non orienté
def voisins(e, node):
    voisins = []
    for i in range(len(e)):
        if e[i][0] == node:
            voisins.append(e[i][1])
        elif e[i][1] == node:
            voisins.append(e[i][0])
    return voisins

# Fonction pour générer un arbre couvrant à partir d'un graphe déconnecté
def arbre_couvrant(v, e):
    visited = []  # Liste pour garder trace des sommets visités
    tree = []  # Liste pour stocker les arêtes de l'arbre couvrant
    # On doit vérifier tous les sommets dans le graphe
    for node in v:
        if node not in visited:
            # Si le sommet n'a pas encore été visité, on lance un DFS à partir de ce sommet
            stack = [node]
            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.append(current)  # Marquer le sommet comme visité
                    for j in voisins(e, current):
                        if j not in visited:  # Si le voisin n'a pas encore été visité
                            tree.append((current, j))  # Ajouter l'arête à l'arbre couvrant
                            stack.append(j)  # Ajouter le voisin à la pile pour exploration
    return tree

# Appeler la fonction pour générer l'arbre couvrant pour tout le graphe
arbre = arbre_couvrant(v, e)
print("Arbre couvrant généré:", arbre)
