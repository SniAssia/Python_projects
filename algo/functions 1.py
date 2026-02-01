"""
def iseven(x):
    if x%2==0:
        return x
    else :
        return "this number is odd "
print(iseven(3))


def iseven (num):
    if num%2 == 0:
        return "n is a even number"
    else:
        return "n is a odd one"
print(iseven(99))


def sum (n):
    count = 0
    sum = 0
    for i in range (n+1):
        count = count + 1
        sum = sum + count
    return(sum)
print(sum(7))

num = 10


def test():
    num = 5
    print(num)
test()
print(num)


def gettotal (n1,n2):
    return n1+n2
print(gettotal(2,3))


def calculator (x,y):
    z = input("enter a math operator: ")
    if z == "+":
        return x+y
    elif z =="-":
        return x-y
    elif z == "*":
        return x*y
    elif z =="/":
        if y==0:
            print("error")
        else:
            return x/y
print(calculator(2,8))


def dot_product(l1,l2):
    square = 0
    for i in range (len(l1)):
        square = square + l1[i]*l2[i]
    return square
print(dot_product([1, 2], [1, 4]))


def function (name,age):
    return name,age
print("assia",12)

def funct1(*var):
    for i in var:
        print(i)
funct1(20,40,50)

"""
"""
def calculate(x,y):
    return x-y,x+y
print(calculate(2,1))

def show(name,salary=9000):
    return name,salary
print(show("ddd",9000))

def sum1(n):
    if n == 0:
        return 0
    elif n > 0:
        return n + sum1(n-1)
print(sum1(10))

def funct(n):
    l1= []
    for x in range (n):
        if x%2 == 0:
            l1.append(x)
    return l1
print(funct(30))


def funct1(list66):

    p = int(input("length of this list :"))
    while (len(list66))<p :
        n = int(input("enter elements "))
        list66.append(int(n))
    return list66
list1 = [ ]
print(funct1(list1))
"""
"""
def convert(n):
    if n >1:
        convert(n//2)
    print(n % 2,end = " ")
print(convert(34))
"""



# Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i),end = " ")




