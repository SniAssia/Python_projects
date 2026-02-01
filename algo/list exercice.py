"""

list1 = [100,200,300,400]
list1.reverse()
print(list1)

#concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = []
for i in range (len(list1)):
    for j in range (len(list2)):
        if i == j :
            list3.append(list1[i]+list2[j])
print(list3)
#the second method
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [i+j for i,j in zip(list1,list2)]
print(list3)

#turn every item of a list into its square
numbers = [1, 2, 3, 4, 5, 6, 7]
squarelist = []
for i in numbers :
    x = i*i
    squarelist.append(x)
print(squarelist)

#concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = []
for i in list1 :
    for j in list2 :
        x = i + j
        list3.append(x)
print(list3)

#iterate both lists simultaneously
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list2.reverse()
for i in range (len(list1)):
    for j in range (len(list2)):
        if i == j :
            print(list1[i] , list2[j],end = " ")
    print()

#remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
list9 = []
for x in list1 :
    if x != "":
        list9.append(x)
print(list9)

#add new item to list after a specified item
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
x=list1[2][2]
x.append(7000)
print(list1)

#extend nested list by adding the sublist
list6 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
x = list6[2][1][2]
x.extend(["h", "i", "j"])
print(list6)

#replace list's item with new value if found
list1 = [5, 10, 15, 20, 25, 50, 20]
for i in range (len(list1)) :
    if list1[i]==20:
        list1[i]=200
print(list1)

#remove all occurrences of a specific item from a list
list1 = [5, 20, 15, 20, 25, 50, 20]
for i in list1 :
    if i == 20:
        list1.remove(i)
print(list1)

#multiply all the items in a list
list9 = [1,6,8,6,6]
square = 1
for i in list9 :
    square = square*i
print(square)

list9.sort()
print(list9[-1])
print(list9[0])
"""

samplelist = ['abc', 'xyz', 'aba', '1221']
emptylist = []
for i in samplelist :
    if i[0]==i[-1] and len(i)>= 2 :
         emptylist.append(i)
print(len(emptylist))




sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

for i in range (len(sample_list)):
    for j in range (i+1,len(sample_list)):
        if sample_list[i][-1]>sample_list[j][-1]:
            sample_list[i], sample_list[j]=sample_list[j], sample_list[i]
print(sample_list)

#write a python program to remove duplicates from a list
list54 = [34,10,55,77,88,88,77,34]
list66 = []
for x in list54 :
    if x not in list66 :
        list66.append(x)
print(list66)

#Write a Python program to check if a list is empty or not.
list1 = []
print(len(list1))
if len(list1)==0:
    print("this list is empty")















