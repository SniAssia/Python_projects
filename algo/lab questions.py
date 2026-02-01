"""
def occur(l):
    dict11={}
    for i in l:
        x=l.count(i)
        dict11[i]=x
    return(dict11)
#call a function
n= int(input("enter the number of elements of these lists : "))
l11= []
for k in range(n):
    num = int(input("enter the elements of these lists "))
    l11.append(num)
print(occur(l11))



def ms(l1,l2):
    i=0
    j=0
    l3=[]
    while i < len(l1) and j < len(l2):
        if l1[i]<l2[j]:
            l3.append(l1[i])
            i+=1
        else :
            l3.append(l2[j])
            j+=1
    return l3
print(ms([1,3,5,7],[2,4,6,8]))

def return_dict(l):
    dict1={}
    for i in l:
        dict1[i]=type(i)
    return dict1
print(return_dict(["1",4.3,"c",123,1.0,1]))

def is_distinct(nb):
    s = str(nb)
    for i in s :
        if s.count(i)>1:
            return False
        return True
print(is_distinct(1941))



#program to find the factor of a number
def factors(n):
    fac=[]
    for i in range(1,n+1):
        if n%i==0:
            fac.append(i)
    return fac
print(factors(8))

def prime(n):
    for i in range (2,n):
        if n%i==0:
            return False
    return True
print(prime(8))




def primes(n):
    l= []
    for i in range(2,n+1):
        if prime(i):
            l.append(i)
    return l
print(primes(19))


#fibonnacci sequence
def fibo(n):
    if n <=1:
        return n
    else :
        return fibo(n-1)+fibo(n-2)

n=int(input("enter the last elements of this sequence : "))
if n<=1:
    print("error")
else :
    for i in range(n):
        print(fibo(i))

#armstrong number
def arm(n):
    s=str(n)
    sum=0
    for i in range(len(s)):
        sum += int(s[i])**len(s)
    return sum
print(arm(135))

#convert decimal to binary using recursion
def bin(n):
    if n<1:
        return n
    elif n>1:
        bin(n//2)
    print(n%2,end = " ")
print(bin(34))


#sum of natural numbers
def sum1(n):
    if n<=1:
        return n
    else :
        return sum1(n-1)+n
print(sum1(16))

#program to add to matrix
x=[[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
y=[[5,8,1],
    [6,7,3],
    [4,5,9]]
a=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range (len(x)):
        a[i][j]=x[i][j]+y[i][j]
print(a)


#transpose a matrix

def trans(r, c):
    l1 = []
    for i in range(r):
        l = []
        for j in range(c):
            num = int(input("enter elements of this matrix: "))
            l.append(num)
        l1.append(l)
    r=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range (len(l1)):
        for j in range(len(l)):
            r[j][i]=l1[i][j]
    return r
print(trans(2,2))


#harmonic sum
def harmo(n):
    if n>1:
        return 1/n+harmo(n-1)
    else :
        return 0
print(harmo(5))


#find pgcd of two numbers
def pgcd(n,b):
    l=[]
    l1=[]
    if n<b:
        for i in range(1,n+1):
            if n%i==0 and b%i==0:
                l.append(i)
        print(l[-1])
    elif  b<n:
        for j in range (1,b+1):
            if b%j==0 and n%j==0:
                l1.append(j)
        print(l1[-1])

    def ppcm (n,b):
        return n*b // pgcd(n,b)
    print(ppcm(12,6))


def pgcd (n,b):
    if n<b:
        n,b=b,n
    while b!=0:
        n,b=b,n%b
    return n
print(pgcd(12,6))


#how to find the maximum of a list using recursive function
def max(L):
    if not L:
        return None
    if len(L)==1:
        return L[0]
    rest_max=max(L[1:])
    if L[0]>rest_max :
        return L[0]
    else:
        return rest_max
print(max([1,2,9,7,8]))



"""
"""
#find the maximum value in a list using recursive function
def maxi(L):
    if len(L)==1:
        return L[0]
    else :
        newlst=maxi(L[1:])
        if L[0]>newlst:
            return L[0]
        else :
            return newlst
print(maxi([1,7,6,0,9,5]))
#add an element to a sorted list using recursive function
def insert(a,L):
    if L==[]:
        L.append(a)
        return L
    elif len(L)==1:
        for i in L:
            if i>a:
                L.insert(0,a)
            else :
                L.append(a)
        return L
    else :
        if L[0]>a:
            return [a]+L
        else :
            return L[0:1]+insert(a,L[1:])
print(insert(5,[1,2,3,4,6,7,9]))

"""
"""
#calculate the number of different way to represent a given amount of money
def coin_combinations(amount, coins):
    if amount < 0:
        return 0
    if amount == 0:
        return 1
    total = 0
    for coin in coins :
        new=amount - coin
        coin_combination= coin_combinations(new, coins)
        total+=coin_combination
    return total
print(coin_combinations(3,[1,2]))


#stochastic matrix
def is_stochastic(P):
    for i in P :
        s=0
        for j in i :
            s+=j
            if s ==1 and j<1 and j>0:
                return True
print(is_stochastic([[0.2,0.8],[0.4,0.6]]))
"""
#display prime numbers less than a number
def prime (n):
    for i in range(2,n+1):
        if n % i == 0:
            return False
    return True
print(prime(9))

def primes (ntherm):
    l = []
    for i in range(2, 100 ** ntherm):
        if prime(i) is True:
            l.append(i)
            if len(l) + 1 > ntherm:
                break
    print(l)


print(primes(5))












