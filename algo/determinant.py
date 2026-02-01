
def submatrix(l,i):
    l3 = []
    for j in range(0, len(l)):
        if j==i:
            continue
        else :
            l2 = []
            for k in range(1,len(l)):
                l2.append(l[j][k])
            l3.append(l2)
    return l3
l3=[[1,3,2],[1,-1,1],[2,1,0]]
def determinant(l):
    if len(l)==1:
        if len(l[0])==1:
            return l[0][0]
    s=0
    for i in range(1,len(l)+1):
        s+=((-1)**(i-1))*determinant(submatrix(l,i-1))*l[i-1][0]
    return s
print(determinant(l3))

