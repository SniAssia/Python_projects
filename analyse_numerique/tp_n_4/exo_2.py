# methode avec pivot partiel

import numpy as np
n=5
np.random.seed(5)
A = np.round( 5*np.random.randn(n,n))

for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j],end="              ")
    print()

def print_m(A):
    print("matrice : ")
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end="               ")
        print()


# definir la matrice elementaire

#M=np.eye(n) #create matrix with 1 in diagonal and 0 everywhere else
# function to generate Mk
def permutation(index1,index2):
    Permut_matrix = np.eye(n)
    Permut_matrix[[index1, index2]] = Permut_matrix[[index2, index1]]
    return Permut_matrix



def generate_mk(A,k,pivot): #parametre matrice A
    Mk= np.eye(n)# k prend des valeurs de 1 a n
    for i in range(k+1,n):
        Mk[i][k]=-A[i][k]/pivot

    return Mk

def generate_lk(Mk,k):
    Lk= np.eye(n)
    for i in range(k+1,n):
        Lk[i][k]= -Mk[i][k]
    return Lk

def recherche_du_pivot(A,k):
    L = A[k:,k]
    # recherche du pivot pour une colonne precise
    pivot = L[0]
    index1=k # index du premier element non nul dans la colonne k
    index2=k
    for i in range(1,len(L)):
        if (abs(L[i])>abs(pivot)):
            index2 =  i+k
            pivot = L[i]
    return pivot , index1,index2




def LU_factor(A,b):
    U = A.copy().astype(float)
    L = np.eye(n)
    b = b.copy().astype(float)
    piv = np.eye(n)
    for i in range(n):
        pivot,index1,index2 = recherche_du_pivot(U,i)
        p = permutation(index1,index2)
        piv = np.matmul(p, piv)
        U = np.matmul(p,U)
        b = np.matmul(p,b)
        Mk= generate_mk(U,i,pivot)
        U = np.matmul(Mk, U)
        b = np.matmul(Mk, b)
        if i > 0:
            L[[index1, index2], :i] = L[[index2, index1], :i]

        L = np.matmul(L, generate_lk(Mk, i))


    return L,U,b,piv
b = np.array([2, 3, 4, 5, 6])
L,U ,b_res,piv= LU_factor(A,b)
print("matrice l: ")
print_m( L)
print("matrice u: ")
print_m(U)
print("vecteur b : ")
for i in range(n):
    print(b_res[i])
print("matrice pivot : ")
print_m(piv)


C = np.matmul(L,U)
print_m(C)
print_m(np.matmul(piv,A))





