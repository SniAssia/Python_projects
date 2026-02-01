
v=[1,2,3,4,5,6,7]
e=[[1,2],[1,4],[1,6],[2,4],[2,3],[3,4],[3,5],[4,5],[4,6],[4,7],[5,7],[6,7]]

def trouver(noeud,e):
    voisins=[]
    for i in range(len(e)):
        if noeud==e[i][0]:
            voisins.append(e[i][1])
        elif noeud ==e[i][1]:
            voisins.append(e[i][0])
    return voisins
def cycle1(v,e):
    visited=[]
    stack=[v[0]]
    elem=stack.pop()
    cycle=[]
    while len(cycle) != len(v):
        if elem not in visited :
            cycle.append(elem)
            visited.append(elem)
            voisins=trouver(elem,e)
            for j in voisins :
                if j not in visited :
                    stack.append(j)
            elem=stack.pop()
    return stack
print(cycle1(v,e))


def cycle1(v,e):
    pile=[(v[0],[v[0]])] # current node and the path to arrive to this node
    while pile :
        visited=[]
        cur,path=pile.pop()
        if len(path)==len(v) and path[0] in trouver(cur,e):
            return path

        for voisins in trouver(cur,e):
            if voisins not in path :
                new=path+[voisins]
                pile.append((voisins,new))
    return None
print(cycle1(v,e))
