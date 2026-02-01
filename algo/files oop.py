#how to find length of a list using recursion
def leng(l):
    if len(l)== 1:
        return 1
    else :
        return 1+len(l[1:])
print(leng([1,8,9,0,67,5,4,8,34,5]))

#find the sum of elements in a list using recursive function
def sum(L):
    for i in L:
        return L[0]+sum(L[1:])
print(sum([1,8,9,6,5,4,9]))









