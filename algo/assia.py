import numpy as np

def lu_decomposition(A):
    """
    Compute the LU decomposition of a square matrix A.
    Returns a tuple (L, U, P) where L is lower triangular, U is upper triangular,
    and P is a permutation matrix such that L * P * U = A.
    """
    n = A.shape[0]
    P = np.eye(n)
    L = np.tril(np.eye(n))
    U = np.triu(np.eye(n))

    for i in range(n):
        for j in range(i, n):
            s = sum(L[i, k] * U[k, j] for k in range(i))
            U[i, j] = A[i, j] - s

        for j in range(i, n):
            if i == j or U[i, j] == 0:
                continue
            s = sum(L[k, i] * U[i, j] / U[i, i] for k in range(i, j+1))
            L[k, j] = (A[k, j] - s) / U[i, j]

        k = np.argmax(np.abs(U[i:, i])) + i
        if k != i:
            U[[i, k], i:] = U[[k, i], i:]
            L[i:, i] = L[i:, k]
            P[[i, k]] = P[[k, i]]

    return L, U, P
print(lu_decomposition([[1,2,3],[4,5,6],[7,8,9]]))