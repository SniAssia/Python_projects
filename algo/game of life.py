# fonction pour chercher les voisins d'une case
# a la ligne , b la colonne
# l=[l[a][b-1],l[a][b+1],l[a-1][b-1],
# l[a-1][b],l[a-1][b+1],l[a+1][b-1],
# l[a+1][b],l[a+1][b+1]]
def chercher1(l,a,b):
    l1=[]
    if 0<=a<=len(l)-1 and 0<=b<=len(l)-1:
        for i in range(-1,2):
            for j in range(-1,2):
                if (i==0 and j==0) or not(0<=a+i<len(l)) or not (0<=b+j<len(l[0])):
                    continue
                else :
                    l1.append(l[a+i][b+j])
    return l1

l=[[1,2,3,4,5,6],
   [7,8,9,10,11,12],
   [13,14,15,16,17,18],
   [19,20,21,22,23,24],
   [25,26,27,28,29,30],
   [31,32,33,34,35,36]]
print(chercher1(l,0,0))
# main function
def gamelife(l):
    for i in range(len(l)):
        for j in range(len(l[i])):
            l1 = chercher1(l,i,j)
            for k in range(len(l1)):
                if l1[k]==0 and sum(l1)==3:
                    l[i][j]=1
                elif l1[k]==1:
                    if sum(l1)<2:
                        l[i][j]=0
                    if sum(l1)==2 or sum(l1)==3 :
                        continue
                    if sum(l1)>=3 :
                        l[i][j]=0
            print(l)
l2=[[1,0,0,1,0,0],
   [0,1,0,0,1,1],
   [1,1,1,1,0,0],
   [0,0,1,1,1,0],
   [0,1,0,1,0,0],
   [1,1,1,0,1,0]]

print(gamelife(l2))

