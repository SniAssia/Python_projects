### systemes triangulaires inferieurs

def resoudre_sys_triangulaire_inf(matrice,vecteur):
    vecteur_sol=[0]*len(vecteur)
    vecteur_sol[0]=vecteur[0]/matrice[0][0]


    for i in range(1,len(matrice)):
        sum=0
        for j in range(0,i):
            sum+=matrice[i][j]*vecteur_sol[j]
            print(sum)
        print()
        vecteur_sol[i]=(vecteur[i]-sum)/matrice[i][i]
    return vecteur_sol
mat=[
    [1, 0, 0, 0, 0],
    [2, 4, 0, 0, 0],   # = 2 * ligne 1
    [3, 6, 9, 0, 0],  # = 3 * ligne 1
    [4, 8, 12, 20, 0], # = 4 * ligne 1
    [5, 10, 15,0,23] # = 5 * ligne 1
]
vecteur =[1,2,3,4,5]
print(resoudre_sys_triangulaire_inf(mat,vecteur))
matrice_test = [
    [2, 0, 0, 0, 0],
    [1, 3, 0, 0, 0],
    [4, -2, 1, 0, 0],
    [0, 5, 2, 4, 0],
    [1, 0, 3, -1, 2]
]

vecteur_test = [4, 5, 6, 7, 8]
print(resoudre_sys_triangulaire_inf(matrice_test,vecteur_test))