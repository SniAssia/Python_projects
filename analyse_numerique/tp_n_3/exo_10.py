## matrice tidiagonale
## resolution de systeme
def calculer(matrice,b):
    n=len(b)
    x =[0]*n
    x[n-1]=(b[n-1]-matrice[n-1][n-2]*(b[n-2]/matrice[n-1][n-1]))/(-matrice[n-1][n-2]*matrice[n-2][n-1]/matrice[n-2][n-2]+matrice[n-1][n-1])
    for i in range(n-2,1,-1):
        x[i]=-x[i+1]*(matrice[i-1][i]/-matrice[i-1][i-2]*matrice[i-2][i-1]/matrice[i-2][i-2]+matrice[i-1][i-1])+


