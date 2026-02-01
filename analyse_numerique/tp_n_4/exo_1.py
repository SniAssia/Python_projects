import numpy as np
n=5
np.random.seed(5)
A = np.round( 5*np.random.randn(n,n))

for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j],end="      ")
    print()

def print_m(A):
    print("matrice : ")
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end="      ")
        print()


# definir la matrice elementaire

#M=np.eye(n) #create matrix with 1 in diagonal and 0 everywhere else
# function to generate Mk

def generate_mk(A,k): #parametre matrice A
    Mk= np.eye(n)# k prend des valeurs de 1 a n

    pivot= A[k][k]
    for i in range(k+1,n):
        Mk[i][k]=-A[i][k]/pivot
    return Mk

def generate_lk(Mk,k):
    Lk= np.eye(n)

    for i in range(k+1,n):
        Lk[i][k]=-Mk[i][k]
    return Lk

def LU_factor(A,b):
    U = A.copy().astype(float)
    L = np.eye(n)
    b = b.copy().astype(float)
    for i in range(n):
        Mk = generate_mk(U,i)
        U = np.matmul(Mk,U)
        b = np.matmul(Mk,b)
        L = np.matmul(L,generate_lk(Mk,i))
    return L,U,b
b = np.array([2, 3, 4, 5, 6])
L,U ,b_res= LU_factor(A,b)
print("matrice l: ")
print_m( L)
print("matrice u: ")
print_m(U)
print("vecteur b : ")
for i in range(n):
    print(b_res[i])

print_m(np.matmul(L,U))







