# creer un arbre couvrant
# refaire cet algo pour n*n !!!
# graphe non orienté
v= [1, 2, 3, 4, 5, 6, 7, 8, 9]
e = [[1, 2], [1, 4], [4, 7], [4, 5], [7, 8],
   [2, 3] , [2, 5], [5, 6], [5, 8], [8, 9], [9, 6], [6, 3]]
def voisins(e,node):
   voisins=[]
   for i in range(len(e)):
      if e[i][0]==node  :
         voisins.append(e[i][1])

      elif e[i][1]==node  :
         voisins.append(e[i][0])

   return voisins
print(voisins(e,6))


def arbre(v,e,node):
   visited=[]
   tree=[]
   stack=[node]
   while stack :
      current=stack.pop()
      if current not in visited :
         visited.append(current)
         for j in voisins(e,current) :
            if j not in visited :
               tree.append((current,j))
               stack.append(j)
   return tree
print(arbre(v,e,1))

def arbre(v,e):
   visited=[]
   tree=[]
   v1=[v[0]]
   node=v[0]
   while len(v1) != len(v):
      l=voisins(e,node)
      for j in range(len(l)):
         if l[j] not in visited:
            tree.append((node,l[j]))
            node= l[j]
            v1.append(l[j])
            visited.append(l[j])

   return tree
print(arbre(v,e))





