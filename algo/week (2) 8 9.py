"""
#while loop
#sum the first 10 numbers
count = 0 # initialize the loop control variable
num =0
while count < 10 :   #check the loop control variable
    count = count + 1   # update the loop control variable
    num = num + count
print(num)

counter = 10
# Initialize loop control variable
# Check the loop control variable
while counter < 10:
    print(counter)
    counter = counter + 1 # Update the loop control variable
print("Outside Loop")
#how to add any 6 numbers
count = 0
sum = 0
while count < 6 :
    count = count + 1
    num = int(input("enter a number :"))
    sum = sum + num
print(sum)
print("average is :", sum/6)
#the average of N number
count = 0
sum = 0
n = int(input("enter a number :"))
while count < n :
    count = count + 1
    num =int(input("enter another number :"))
    sum = sum + num
print(sum )
print("the average of these numbers is : ",sum/n)

#the sum of all even numbers less than 50
count = 0
sum = 0
while count <= 50 :
    count = count + 2
    sum = sum + count
print(sum )  """
"""
#multiplication table of a number n
count = 1
n = int(input("enter a number :"))
while count < 10:
    count = count + 1
    print(n,"*",count,"=",n*count)


import math
count = 0
result =1
result2 = 1
N = int(input("Enter a strict positive number :"))
while count < N :
    count = count +1
    result = result*count
    result2 = 1/result

print(result2)

import math
n = int(input("Enter a strict positive number :"))
count = 0
result = 1
while count <= n :
    count = count + 1
    result = 1/math.factorial(count)
    sum = result +  1/count
    print(sum)


stream = "software "
for letter in stream :

    print(letter)

weekdays = ['monday','tuesday','wednesday']
for x in weekdays :
    print(x)

for num in range (10):

    if num ==5 :
        continue
    print(num)
print("out of logo")

#nested loop

numlist = ['1','2','3']
alphalist = ['a','b','c']
for i in numlist :
    for j in alphalist :
        print(i,j)
n = int(input("enter a number :"))
for i in range (2,n):
    if n % i == 0:
        print(n,"is not a prime number ")
        print(i,'times',n//i,"is",n)
        break
    else:
        print(n,"is a a prime number ")
"""
#ask the user to keep entering as many numbers as she wants
positiveNum = 0
negativeNum = 0
evenNum = 0
divisible_7 = 0
ask = "yes"
while ask == "yes":
    n =int(input("enter an integer:"))
    if n > 0:
        positiveNum = positiveNum + 1
    elif n < 0 :
        negativeNum = negativeNum + 1
    elif n%2 == 0:
        evenNum = evenNum + 1
    elif n%7==0:
        divisible_7 = divisible_7 + 1
    ask = input("add a number ")
print(positiveNum)
print(negativeNum)
print(evenNum)
print(divisible_7)


#write a python program to display all prime numbers within a range

a = int(input("enter an integer :"))
b = int(input("enter another integer :"))

print("prime numbers between ",a ,"and",b ,"are :")
for n in range (a,b+1):
    if n>1:
        for i in range (2, n ):
            if n%i==0 :
                break
        else:
            print(n)


a = int(input("enter an integer :"))
b = int(input("enter an integer :"))
for n in range (a,b+1):
    if n>1 :
        for i in range (2,n):
            if n%i==0:
                break
        else :
            print(n)







