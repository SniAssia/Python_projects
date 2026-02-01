import numpy as np


def generate_mk(A, k):
    n = len(A)
    Mk = np.eye(n)
    pivot = A[k][k]
    for i in range(k + 1, n):
        Mk[i][k] = -A[i][k] / pivot
    return Mk


def generate_lk(A, k):
    Lk = np.eye(len(A))
    pivot = A[k][k]
    for i in range(k + 1, len(A)):
        Lk[i][k] = A[i][k] / pivot
    return Lk


def LU_factor(A, b):
    n = len(A)
    U = A.copy().astype(float)
    L = np.eye(n)
    b = b.copy().astype(float)

    for k in range(n):
        Mk = generate_mk(U, k)
        Lk = generate_lk(U, k)
        U = Mk @ U
        b = Mk @ b
        L = L @ Lk

    return L, U, b


# Test your function
np.random.seed(5)
n = 5
A = np.round(5 * np.random.randn(n, n))
b = np.array([2, 3, 4, 5, 6])

L, U, b_mod = LU_factor(A, b)

print("Matrix A:")
print(A)
print("\nL matrix:")
print(L)
print("\nU matrix:")
print(U)
print("\nModified b after forward substitution:")
print(b_mod)
