# define the function
def greet(name):
    print("hello,"+name+".Good mornin")
num = input("enter your name :")
#call the function
greet(num)

# define function with two arguments
def greet (name,msg):
    print("hello",name,",", msg)
#call the function
greet("assia","good morning")

#sum three numbers
def sum (num1,num2,num3):
    return num1 + num2 + num3
#call function
print(sum(4,5,6))


#returns absolute value
def absolute(num):
    if num >= 0:
        return num
    else :
        return -num
#function call
print(absolute(-5))

#the greatest number of three numbers
def great_num (num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3:
        return num2
    else :
        return num3
#function call
print(great_num(6,4,5))

#even number or not
def evennum(num):
    if num%2==0:
        return True
    else :
        return False
print(evennum(9))

#sum of all numbers from 1 to n
def sum_n (n):
    count = 0
    sum = 0
    while count< n :
        count = count + 1
        sum = sum + count
    return sum
print(sum_n(8))

num = 10
def test():
    num = 5
    print(num)
test()
print(num)

#sum of two numbers
def getTotal(num1,num2):
    return num1 + num2
print(getTotal(8,9))

def reversedigit(num1):
    result = str(num1)
    return result[::-1]
print(reversedigit(12345))

sum = 0
for c in range(3):
    if c ==1 :
        continue
    sum = sum + c
print(sum/c)


def factorial (n):
    if n == 1 :
        return n
    else :
        return n*factorial(n-1)
print(factorial(7))

#program that acts as a simple calculator
ask = "yes"
while True:
    def add(x,y):
        return x+y
    def subtract (x,y):
        return x - y
    def division (x,y):
        if x != 0:
            return x/y
        else :
            print("error")
    def multiplication (x,y):
        return x*y
print(add(1,9))
print(subtract(1,9))
print(division(7,8))
print(multiplication(1,8))
#write functions with good documentation and use the sentinal loop to let the user repeats as many times as sche wants
