
""""
score = float(input("Enter the score of this student :"))
if score>=60 :
    print("Passed")
else :
    print("Failed")
x = float(input("Enter a number :"))
if x > 0 :
    print("This number is positive")
else :
    print("This number is negative")
x = int(input("Enter a number :"))
if x >0:
    print("The absolute value of ths number is :",x)
else :
    print("The absolute value of this number is :",-x)
x = int(input("Enter a number : "))
y = int(input("Enter another number : "))
if x==y :
    print(x and y ,"are equal")
elif x<y :
    print(y,"is greater")
else :
    print(x,"is greater")

x =int(input("Enter first number :"))
y = int(input("Enter second number :"))
z = int(input("Enter the last number :"))
if x ==y==z :
    print(x and y and z,"are equal")
elif x>y and x>z :
    print(x,"is greater")
elif y>z :
    print(y,"is greater ")
else :
    print(z,"is greater ")

temper = float(input("Enter the temperature inside :"))
if temper > 45 :
    print("you should do some indoor activities :")
elif temper >30 and temper <45:
    print("take some appropriate precaution ")
else :
    print("lets hang out ")


x = int(input("enter a number :"))
if x%2 = 0 :
    print(x,"is an odd number ")
else :
    print(x,"is an even number ")
grade = float(input("enter your grade :"))
if grade >= 90 :
    print("A")
elif grade>=80 :
    print("B")
elif grade>= 70 :
    print("C")
elif grade>=60 :
    print("D")
else :
    print("F")
print("have a nice day ") """
""""
sent = input("enter a sentence :")
if sent[0]=="a" or sent[0]=="o" or sent[0]=="i" or sent[0]=="u"or sent[0]=="e" :
    print(sent)
else :
    print(sent.capitalize())"""
""""
sent=input("enter a string :")
sent2 = input(sent[0:2])
sent3 = input(sent[-3:-1])
if len(sent2+sent3)<4:
    print(sent[0:2] + sent[-3:-1])"""
""""
#nested if :
x = int(input("enter the first side of a triangle :"))
y = int(input("enter the second side of this triangle :"))
z = int(input("enter the third side of this triangle :"))
if x+y> z and x+z>y and y+z>x :
    print("this three sides form a triangle .")
    if (x**2)+(y**2)==(z**2) or (x**2)+(z**2)==(y**2) or (z**2)+(y**2)==(x**2):
        print("this is a right angled triangle ")
    elif x==y==z:
        print("this triangle is equilateral ")
    elif x==y or x==z or z==y :
        print("this triangle is isosceles")
    elif x != y and x != z :
        print("this triangle is scalene ")
else :
    print("this is note a triangle .")"""
"""
hours = int(input("enter number of hours that worked this person this month :"))
salForOne=float(input("enter your salary for one hour  :"))
if hours> 40:
    print("your salary is :",salForOne*1.5*hours)
else :
    print("your salary is :",salForOne*hours)  """
""""
str = input("enter your name :")
if str == "assia" :
    print("great")

time = int(input("enter time :"))
if time >= 0000 and time<=1200 :
    print("good morning")
elif time >1200 and time <= 1700:
    print("good afternoon")
elif time >1700 and time <= 2100:
    print("good evening")
else :
    print("good night")"""


count = 0  #initialize loop control variable
num = 0
while count < 10 :  #check the loop control variable
    count = count + 1
    num = num  + count

print(num)




















