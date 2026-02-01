# algorithme de tri topologique
V = [1, 2, 3, 4, 5, 6, 7]
E = [[2,5], [5,6], [2,7], [5,1], [1,4], [6,3], [7,4], [4,3]]
# fct qui verifie si un noeud n'a pas de fleche entrante
def check(node,e):
    loop =1 # ce noeud existe
    for i in range(len(e)):
        if node == e[i][1]:
            loop=0 # ce noeud n'existe pas
            break
    return loop
# fonction qui trouve un noeud sans fleche entrante
def trouver(v,e):
    var=-1
    for i in range(len(v)) :
        if check(v[i],e)==1: # node sans fleche entrante
            var= v[i]
            break
    return var


# enelever les fleches mortes
def enlever(v,e):
    for i in e :
        if (i[0] not in v) or (i[1] not in v ):
            e.remove(i)

# algo rincipal
def general(v,e):
    l=[]
    while 1 :
        retour =trouver(v,e)
        if retour == -1:
            break
        l.append(retour)
        v.remove(retour)
        enlever(v,e)
    if len(v) != 0:
        print("-1")
    else :
        print( l)
print(general(V,E))

# n nbre de noeuds
# m nbre de fleches
# check o(m)
# trouver o(n*m)
# enlever  o(m)
# general o(n*n*m)
# Si m = O(n²) (maximum possible de flèches) :
# ==> Complexité O(n^4)

