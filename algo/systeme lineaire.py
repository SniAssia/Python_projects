M = []
M.append([3, -3, 2, 2, 2, 1])
M.append([-2, 2, 3, -2, -1, -1])
M.append([-2, 3, -2, -1, -1, 1])
M.append([3, 2, -3, -2, -3, 1])
M.append([3, 3, 1, 1, -3, -1])
M.append([2, -3, -3, 3, 2, 1])

b=[35,-1,12,20,-56,-12]
def echelonner(m,b):
    for i in range(len(m)):
        elem = m[i][i] # pivot
        if elem != 0 :
            for k in range(i+1,len(m)):
                mi=m[k][i]/elem
                for j in range(i,len(m)):
                    m[k][j]-=mi*m[i][j]
                b[k]-=mi*b[i]
    # trouver les valeurs des x :
    n=len(m)
    x=[0]*n
    for i in range(n-1,-1,-1):
        if m[i][i] != 0:
            x[i]=b[i]/m[i][i]
            for j in range(i-1,-1,-1):
                b[j]-= x[i]*m[j][i]
    return x
print(echelonner(M,b))






