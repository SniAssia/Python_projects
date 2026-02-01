
#create a list
mylist = ["monday","tuesday","lolo","ee",2,67,90]
#reverse the list
mylist.reverse()
print(mylist)
print(mylist.count(2))
print(len(mylist))
mylist1 =[11,88,77,67,56,90,0,64]
mylist1.sort()
mylist1.reverse()
print(mylist1)
list1 = ["monday","hoho"]
list2 = [11,66]
#adding two lists
list3 = list1 + list2
print(list3)
list = ["sunday","monday","tuesday","wednesday",66]
for i in list :
    print(i)
print("sunday" in list)
print("hello" not in list)
for j in range (len(list)):
    print(j)
#sum of list elements
list4 = [11,88,66,2,3,5,7]
sum = 0
for i in list4 :
    sum = sum + i
average = sum / i  #or average = sum / len(list4)
print(sum)
print(average)
#steps to create a list
#ask the user to enter the size of a list and also the elements of the list
n = int(input("enter the size of the lisit:"))
list8 = []
for i in range (0,n):
    num = input("enter elements of this list :")
    list8.append(num)
print(list8)
#remove duplicates from a list
list9 = ["baana",66,99,66,88,"baana"]
newlist7=[]
for i in list9 :
    if i not in newlist7 :
        newlist7.append(i)
print(newlist7)


#we can convert a string s elements to a list to have the ability to do a lot of modifications
name = input("enter a sentence :")
newwlist = name.split()
print(newwlist)
newwlist0= name.split("o")
print(newwlist0)
#split a words list and count the number of words
sent = input("enter a sentence :")
liist = sent.split()
print(liist)
print(len(liist))
#first methode
mylist = [100,677,77,88,777,543,90,87]
oldlist = []
for i in mylist :
    if i < 100:
        oldlist.append(i)
print(oldlist)
#second methode
mylist = [100,677,77,88,777,543,90,87]
for i in range (len(mylist)):
    if mylist[i]>100:
        mylist[i]= 0
print(mylist)
#nested list
nlist = [1,8,89,"mooo",[1,8,9]]
print(nlist[0])
print(nlist[4][2])

#represent matrices
matrice = [[1,2,3],[1,7,0],[4,67,8]]
for i in range (len(matrice)):
    for j in matrice[i]:
        print(j, end = " ")
    print()
#sum of matrices elements
sum = 0
mx = [[1,6,8],[8,0,6],[7,7,9]]
for i in range (len(mx)):
    for j in mx[i]:
        sum = sum + j
print(sum)
#concatenate two lists index wise
list1 = ["m","na","i","ke"]
list2 = ["y","me","s","sy"]
odlist= []
for i in range (len(list1)) :
    for j in range (len(list2)):
        if i == j :
            odlist.append(list1[i]+list2[j])
print(odlist)

#turn every item of a list into its square :
numbers = [1, 2, 3, 4, 5, 6, 7]
nali = []
for i in numbers :
    square = i**2
    nali.append(square)
print(nali)
