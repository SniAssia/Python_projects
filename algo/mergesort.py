import random
# coder la foncton merge
def merge(l1,l2):
    l3=[]
    p1=0
    p2=0
    loop=1
    while loop==1:
        if p1<len(l1) and p2<len(l2):
            if l1[p1]>l2[p2]:
                l3.append(l2[p2])
                p2+=1
            else :
                l3.append(l1[p1])
                p1+=1
        elif p1>=len(l1) and p2<len(l2):
            l3.append(l2[p2])
            p2+=1
        elif p1<len(l1) and p2>=len(l2):
            l3.append(l1[p1])
            p1+=1
        elif p1>=len(l1) and p2>=len(l2) :
            loop =0
    return l3
l1=[1,6,8,70]
l2 =[2,7,9,56]
print(merge(l1,l2))
# how to sort a list
def mergedsort(l):
    if len(l)<=1:
        return l
    else :
        mid=int(len(l)//2)
        l1 = l[0,mid-1]
        a=mergedsort(l1)
        l2=l[mid,len(l)-1]
        b=mergedsort(l2)
        return merge(a,b)
# merge sort non-recurssif
# List à trier
# approche bottom-up
l=[76, 13, 55, 18, 23, 17, 28, 84,2]
def merge_pair(l):
    if len(l) % 2 == 0:
        dict={(i,j):[] for i in range(1,len(l)//2) for j in range(len(l)//(2*i))}
        for i in range(len(l)):
            dict[0,i]=[l[i]]
        for i in range(1,len(l)//2):
            for j in range(0,len(l)//(2*i)):
                dict[(i,j)]= merge(dict[i-1,2*j],dict[i-1,2*j+1])
        return dict[len(l)//2-1,0]
def merge_non(l):
    if len(l) % 2 == 0:
        return merge_pair(l)
    else :
        l1=[]
        for i in range(len(l)-1):
            l1.append(l[i])
        return merge(merge_pair(l1),[l[len(l)-1]])

print(merge_non(l))
"""  list1 = [10, 20, 30]
list2 = ['a', 'b', 'c']
# Using zip to combine indexes with the values
for index, (item1, item2) in enumerate(zip(list1, list2)):
    print(index, item1, item2)
Output:
0 10 a
1 20 b
2 30 c """

"""
list1 = [10, 20, 30]
list2 = ['a', 'b', 'c']
# Iterate over both lists with independent indexes
for (idx1, item1), (idx2, item2) in zip(enumerate(list1), enumerate(list2)):
    print(f"list1[{idx1}] = {item1}, list2[{idx2}] = {item2}")
Output:
list1[0] = 10, list2[0] = a
list1[1] = 20, list2[1] = b
list1[2] = 30, list2[2] = c"""
# divide the list k times and not 2 times
l=[76, 13, 55, 18, 23, 17, 28, 84,2]
def div_k(l,k):
    if k*2<len(l):
        re=len(l) % k
        dict1 = {i: [] for i in range(0, len(l) - len(l) // k + 1, len(l) // k)}
        for i in range(0,len(l)-len(l)//k+1,len(l)//k):
            for j in range(len(l)//k):
                dict1[i].append(l[i+j])
                print(dict1)
        for i in range(len(l)-re,len(l)):
            dict1[next(reversed(dict1.keys()))].append(l[i])
            # next(reversed(dict.keys()) help us to get the last element of a dict
        return dict1
    else:
        re = len(l) % k
        dict1 = {i: [] for i in range(k)}
        for i in range(len(l)-re):
            dict1[i]=[l[i]]
        for j in range(len(l)-re,len(l)):
            dict1[next(reversed(dict1.keys()))].append(l[j])
        return dict1
print(div_k(l,2))
# merge k lists
def merge_k(l,k):
    dict1 = div_k(l, k)
    l1 = list(dict1.values())
    l2=[]
    l2.append(l1)
    while len(l1) > 1:
        merged_list = []
        for i in range(0, len(l1), 2):
            if i+1< len(l1):
                merged_list.append(merge(l1[i], l1[i + 1]))
            else:
                merged_list.append(l1[i])

        l1 = merged_list
    return l1
print(merge_k(l,3))


# tri par selection
# cherche le minimum
# - l'ajouter à une nouvelle liste
# - cherche le nouveau minimum
# - etc..
dict={1:2,3:4}
