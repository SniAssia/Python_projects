import math
import numpy as np
# on a A mtrice definie positive on cherche a la decomposer en L*L transposée
# L matrice triangulaire inferieure

def cholesky(A):
    n = len(A)
    L = np.zeros_like(A)  # matrice L initialisée à zéro

    for k in range(n):
        L[k][k]=math.sqrt(A[k][k])
        for j in range(k+1,n):
            L[j][k]=A[j][k]/L[k][k]
            for i in range(k+1,j):
                A[i][j]-=L[i][k]*L[j][k]
    return L

A = np.array([
    [6, 3, 4, 2, 1],
    [3, 6, 5, 1, 2],
    [4, 5, 10, 3, 2],
    [2, 1, 3, 8, 4],
    [1, 2, 2, 4, 7]
], dtype=float)
def print_m(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end="      ")
        print()
L = cholesky(A)
K = L.transpose()
print_m(np.matmul(L,K))



# SECOND METHOD
a = np.array([1,2,3,4,5])
a_t = a.transpose()
# np.block pour construire b en block
B = np.block([
    [np.array([[222]]), a_t.reshape(1, -1)],
    [a.reshape(-1, 1), A]
])
def chol_n1(B):
    n= len(B)
    L = np.zeros_like(B)
    L[0][0]= math.sqrt(B[0][0])
    L[1:,0]= B[1:,0]*(1/L[0][0])
    # reshape(-1,1) vecteur colonne n×1
    # reshape (1,-1) vecteur ligne 1×n
    Q = np.matmul(L[1:,0].reshape(-1,1),L[1:,0].reshape(1,-1))
    L[1:,1:]= cholesky(A-Q)
    return L
C = chol_n1(B)
print_m(C)
print("3##############################")
print_m(np.matmul(C,C.transpose()))