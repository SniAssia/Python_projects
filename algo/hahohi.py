"""
r=0
s=0
while r<50:
    s=s+r
    r=r+2
print(s)
#multiplication of number
count = 0
n=int(input("enter a number : "))
while count <10:
    count = count + 1
    s=n*count
    print(n,"*",count,"=",s)
#check if a number is prime or not
n= int(input("enter a number : "))
if n>1:
    for  i  in range(2,n):
        if n%i==0:
            print("this is not  a prime number ")
            break
        else :
            print("this is a prime number : ")
            break

positive = 0
negative = 0
even = 0
divisible = 0
while True :
    num = input("enter a number : ")
    if num=="quit ":
        break
    if num >0:
        positive=positive +1
    if num<0:
        negative+=1
    if num%2==0:
        even+=1
    if num%7==0:
        divisible+=1
print(positive,negative,even,divisible)
"""
"""
#all prime numbers between 1 and 500
for i in range(3,500):
    for j in range(2,i):
        if i%j==0:
            break
    else :
        print(i)
def sorted(list):
    n= len(list)
    for i in range(n):
        for j in range(n-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]

    return list
print(sorted([8,9,6,4,0]))

#how to remove duplicates from a  list
l=[]
n= int(input("enter lenght: "))
for i in range(n):
    o=input()
    l.append(o)
print(l)
l1=[]
for i in l:
    if i not  in l1:
        l1.append(i)
print(l1)

"""
name = "School of Computer Science"
myList = name.split()
print(myList)
myList = name.split('o')
print(myList)
myList = name.split('ol')
print(myList)

#how to represent a matrix
mx=[[1,2,3],[5,6,7],[8,9,0]]
for i in mx:
    for j in i :
        print(j,end = " ")
    print()


#the sum of elements in a matrix
mx=[[1,2,3],[5,6,7],[8,9,0]]
s=0
for i in mx:
    sum=0
    for j in i :
        sum=sum+j
    s=s+sum
print(s)

def bas(base,num):
    r=""
    if num<2:
        return "invalid syntax"
    elif num>2:
        num%base
        r=r+bas(base,num//base)
    return r
print(bas(2,10))

