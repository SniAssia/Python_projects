#quick sort
def quicksort(l):
    if len(l)<=1:
        return l
    else:
        pivot = l[0]
        l1=[] #listes des elements qui sont plus petits que le pivot
        l2=[] #listes des elements qui sont plus grands que le pivot
        l3=[] # listes des elements qui sont egaux au pivot
        for i in range(len(l)):
            if l[i]<pivot :
                l1.append(l[i])
            elif l[i]==pivot :
                l2.append(l[i])
            elif l[i]>pivot :
                l3.append(l[i])
        a1=quicksort(l1)
        a2=quicksort(l2)
        a3=quicksort(l3)
        return a1+a2+a3

#compteur d'etapes de calcul
# 1+1/2+1/4+...=2
# iteratif

l=[7,8,1,2,3,2,23]
def partitionner(l,id_piv):
    pivot=l[id_piv]
    l1=[]
    l2=[]
    for i in range(len(l)):
        if l[i] < pivot:
            l1.append(l[i])
        elif l[i]> pivot:
            l2.append(l[i])
    return l1 , [pivot] , l2

def quick_sort_2(l):
    stack = [(0,len(l)-1)]
    result=l[:]
    while stack :
        start,end = stack.pop()
        if start<end :
            id_pivot1= (start+end)//2
            left , pivot , right = partitionner(result[start:end+1] , id_pivot1-start)
            result[start:end+1]= left+ pivot+ right
            stack.append((start,start+len(left)-1))
            stack.append((start+len(left)+1,end))
    return result
print(quick_sort_2(l))

