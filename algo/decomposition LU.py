
# create a program to find the decomposition of a square
# matrix into to matrix L and U
# first step : ask the user to enter elements of our main matrix
ord = int(input("enter the order of this square matrix : "))  # ask the user to enter the order
l=[]
for i in range (ord):
    l1=[]
    for j in range(ord):
        # ask the user to enter elements of our matrix
        elements = int(input("enter elements of our matrix : "))
        l1.append(elements)
    l.append(l1)
print(l)  # ask the user to print the final result of our matrix
# second step : apply the rule to decompose this matrix into to matrix
#define a function to find the lu decomposition

def transvection(M,i,j):
    M[i]=[M[i][k]-(M[i][0]/M[0][0])*M[j][k] for k in range(len(M[i]))]
    return M

def findU(M):
    for i in range(1,len(M)):
        L1=transvection(M,i,0)
    return L1

def findU1(M,r,c):
    for i in range(r):
        for j in range(c):
            if r>c:
                L2=findU(M)
    return L2
print(findU1(l,len(l),len(l)))

""""
def lu(A):
    for i in range (len(A)):
        for j in range (1,len(A)):
            if A[0][0]!=0:
                s=A[i][j]/A[0][0]
                A[i][j]-=s

    return A
print(lu(l))
"""






