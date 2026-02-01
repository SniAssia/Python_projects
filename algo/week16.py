"""
l1=[]
n = int(input("enter the number of children in one line : "))
for i in range(n):
    l2=[]
    k=int(input("enter the length of every list : "))
    for j in range(k):
        num = input("enter a digit that refer to every students : ")
        l2.append(num)
    l1.append(l2)
print(l1)

def file():
    file = open("bill.txt","w")
    for element in l1 :
        file.write(element+ "\n")
    file.close()
file()

l1=[]
k=int(input("enter how many numbers you want to change:"))
for j in range(k):
    l2=[]
    for i in range(2):
        num = input("enter the number and its base : ")
        l1.append(num)
    print(l1)
def file():
    file = open("bill.txt","w")
    for element in l1 :
        file.write(element+ "\n")
    file.close()
file()


def convert_to_base(n, base):
    if n == 0:
        return '0'
    result = ''
    while n > 0:
        remainder = n % base
        result = str(remainder) + result
        n //= base
    return result

def palindrome(n,base):
    s=str(convert_to_base(n, base))
    h=len(s)//2
    if s[0:h] == s[-1:h]:
        return True
    return False
print(palindrome(52,10))
"""

"""
# Author(s): assia snissi

# Date of Creation: 13_12_2023


# open sample.txt to read from
handle = open ("input", "r")
for i in handle :
    l=i.split()
    print("the number of words in this file is : " ,len(l))
handle = open ("sample.txt", "r")
# read all content of the file
text = handle.read()
# print variable text to screen
print(text)
# close file
handle.close()

"""

class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def multi(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sub(self):
        return self.a-self.b
a=int(input("enter value of a : "))
b=int(input("enter the value of b :"))
obj=cal(a,b)
choice = 1
while choice!=0:
    print("0.exit")
    print("1.add")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    choice = int(input("enter a choice : "))
    if choice ==1:
        print("result:",obj.add())
    elif choice ==2:
        print("result:",obj.sub())
    elif choice ==3:
        print("result:",obj.mul())
    elif choice ==4:
        print("result",round(obj.div(),2))
    else :
        print("invalid")
print()

import math
class circle():
    def __init__(self,r):
        self.r=r
    def area(self):
        return math.pi*(self.r**2)
    def peri(self):
        return math.pi*2*self.r
r=float(input("enter radius of this circle : "))
obj=circle(r)
print("area of circle : ",round(obj.area(),2))
print("perimeter of circle :",round(obj.peri(),2))

#write a python program to find the area of rectangle using classes
class circle():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def area(self):
        return self.a*self.b
a=int(input())
b=int(input())
obj=circle(a,b)
print("area of circle is : ",round(obj.area(),2))
print()



