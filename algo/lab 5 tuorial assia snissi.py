
#Q1

#fibonacci sequence
n = int(input("enter the number of terms of this sequence :"))
#n should be a positive number
if n < 0 :
    print("invalid number , please enter a positive integer .")
#check the case when n equalto 0
elif n == 0:
    print("the fibonacci sequence is : 0")
#check the case when n equal to 1
elif n == 1:
    print("the fibonacci sequence is : 0 , 1, 1")
else:
#initialize the value of variables by giving the three first numbers of this sequence
    num_before = 0
    number = 1
    next_number = 1
    count = 0
    while count < n :  #the loop will generate numbers until the value of the counter is equal to n
        count = count + 1
        num_before = number
        number = next_number
        next_number = num_before + number
        print(next_number)  #the output will be a list of numbers called fibonacci sequence that satisfy the conditions required

#Q2
#amstrong Number
#_write a python program to check armstrong number
#enter a number containing just three digits
num = int(input("enter a positive number contains 3 digits :"))
#store this number in astring in order to find location of ay dgit easily
string_num = str(num)
#store the three digits in another variables
x = int(string_num[0])
y = int(string_num[1])
z = int(string_num[2])
#put armstrong numbers condition and verify if the number satisfy it or not
if (x**3)+ (y**3) + (z**3) ==num:
    print("this is an armstrong number ")
else :
    print("this is not an armstrong number ")

#factorial_number
#Q3
count = 0   #initialize the loop control variable
iresult = 1
#store an integer in a variable to find its factorial (n!)
n = int(input("Enter a positive number :"))
while count < n:     #check the loop control variable
    count = count + 1     #update the loop control variable
    iresult = iresult * count    #the square of n first numbers
print("the factorial of :",n ,"is", iresult)

#Q4
#sum of a serie
import math  #we display import math to use some mathematical operations like factorial
#store the last integer that will appear in sum in a varable
n = int(input("Enter a strict positive number :"))
#initialize the loop control variable
count = 1
result = 0
#check the loop control variable
while count <= n :
    result = result + 1/math.factorial(count)
    count = count + 1   #update the loop control variable
print("the sum of this serie is :",result)


