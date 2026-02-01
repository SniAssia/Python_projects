l= [344,
433,
434,
444,
334,
343,
333,
443
]
#il doit retourner le nombre qui existe dans la position pos
def find_pos(n,pos):
    sum=0

    for i in range(pos):
        prod = 1
        sum = n//10
        prod=n%10
        n=sum
    return prod
print(find_pos(123456789,3))
def radix_sort(l):
   m=len(str(l[0]))
   for i in range(len(l)):
       if len(str(l[i]))>m:
           m =len(str(l[i]))
   for j in range(1,1+m):
       l1 = []
       for i in range(10):
           l1.append([])
       for i in range(len(l)):
           l1[find_pos(l[i],j)].append(l[i])
       l3=[j for i in l1 for j in i ]
       l=l3
   return l
print(radix_sort(l))