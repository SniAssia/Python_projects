#python program to print the fibonacci sequence
"""
def fib_sequence(n):
    if n <= 1:
        return n
    else :
        return fib_sequence(n-1) + fib_sequence(n-2)
print("fibonacci sequence is : ")
for i in range (10):
    print(fib_sequence(i),end = " ")

#function to find the factorial of a number
def factorial(n):
    if n <= 2 :
        return 1
    else :
        return n * factorial(n-1)
for i in range (10):
    print(factorial(i))

#armstrong number
def arm(n):
    if int(n) < 10:
        return int(n)
    else :
        s = str(n)
        sum = 0
        for i in range(len(s)) :
            sum += int(s[i]) ** len(s)
    return sum
print(arm(153))


#create a function to convert decimal to binary system
def bin_system(n):
    if n <= 1 :
        return str(n)
    else :
        bin_system(n//2)
        return  bin_system(n//2) +" "+ str(n%2)
print(bin_system(9))


#create a function to find the factors of a number
def factor (n):
    for i in range(2,n):
        if n%i!=0:
            return n
        else :
            factor(n//i)
            return i , factor(n//i)
ntherms = int(input("enter a positive integer : "))
print(factor(ntherms))


#create a function to transpose a matrix
#create a program that display your nested lists (matrixes)
def lists(c,r):
    l2= []
    for i in range (r) :
        x = []
        for j in range (c) :
            rows = input("enter the value of rows :")
            x.append(rows)
        l2.append(x)
    l5 = []
    for l in range (c):
        l9 = []
        for k in range(r):
            l9.append(l2[k][l])
        l5.append(l9)
    return l5
print(lists(3,3))

#program to sort words in alphabetic order
def ord(word):
    s = word.split()
    s.sort()
    for i in s :
        print(i,end = " ")
print(ord("what is your first meal "))
"""
#program to count the number of each vowel

def coin_combinations(amount, coins):
    if amount == 0:
        return 1
    if amount < 0 or not coins:
        return 0
    return coin_combinations(amount, coins[1:]) + coin_combinations(amount - coins[0], coins)

# Test cases
print(coin_combinations(3, [1, 2])) # 4
print(coin_combinations(25, [1, 5, 10, 25])) # 13
print(coin_combinations(50, [1, 5, 10, 25])) # 61

