v=[1,2,3,4,5,6]
e=[[1,2],[1,3],[2,3],[2,4],[3,5],[4,5],[2,5],[4,3],[3,6],[5,6]]
# checker si ce graphe est connexe ou non

def voisins(e,node):
   voisins=[]
   for i in range(len(e)):
      if e[i][0]==node  :
         voisins.append(e[i][1])

      elif e[i][1]==node  :
         voisins.append(e[i][0])

   return voisins
# parcourir le graphe a partir d'un sommet si je visite tous les
# sommets le graphe est liée
def check(sous_graphe,e):
    vis=[]
    vis.append(sous_graphe[0])
    sommet = sous_graphe[0]
    for i in range(1,len(sous_graphe)):
        if sous_graphe[i] in  voisins(e , sommet):
            vis.append(sous_graphe[i])
            sommet = sous_graphe[i]
    if len(vis) != len(sous_graphe):
        return 0
    else :
        return 1

def main_func(v,e):
    l0=[]
    for k in range(len(v)):
        i=0
        l=[]
        while  i < len(v):
            for j in range(i,i+1):
                l.append(v[j])
            if check(l,e)==0:
                l.pop()
                i+=1
            elif check(l,e)==1:
                i+=1
        l0.append(l)
        a=v.pop(0)
        v.append(a)
    return l0
print(main_func(v,e))










