"""
#how to convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict1={}
for i in range(len(keys)):
    dict1[keys[i]]=values[i]
print(dict1)

#merge two python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
merged_dict = {**dict1, **dict2}
print(merged_dict)

#print the value of key history from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict['class']['student']['marks']['history'])
#initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
dict = {}
for i in employees :
    dict[i]=defaults
print(dict)


#create a dictionary by extracting the keys from a given dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
newdict  ={}
newdict.update({"name":"kelly","salary":8000})
print(newdict)
keys = ["name","salary"]
for k in keys :
    sample_dict.pop(k)
print(sample_dict)

#check if a value exists in a dictionary
sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():
    print("200 present in a dict")
"""
"""
#convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict = {}
for i in range (len(keys)):
    dict[keys[i]]=values[i]
print(dict)

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = {**dict1,**dict2}
print(dict3)

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
dict3 = dict.fromkeys(employees,defaults)
print(dict3)

#we have this dict and we wanna take some elements from this list and update it to another empty dict

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
#insert keys of elements that you wanna insert in your dict and display it in a list
keys = ["name","age"]
dict66 = {}
for k in keys :
    dict66.update({k:sample_dict[k]})
print(dict66)
#delete a list of keys from a dictionnary
dict68= {}
keys1 = ["name","age"]
for k in sample_dict :
    if k not in keys1:
        dict68.update({k: sample_dict[k]})
print(dict68)
#check if a value exists in a dictionary
sample_dict = {'a': 100, 'b': 200, 'c': 300}
for k in sample_dict :
    if sample_dict[k]==200:
        print("200 present in a dict")
#rename key of a dictionary
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
dict78 ={}
list5 = ["name","age","salary"]
for k in sample_dict :
    if k in list5 :
        dict78.update({k:sample_dict[k]})

dict78.update({'location':'newyork'})
print(dict78)

#Get the key of a minimum value from the following dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
list66 = []
for k in sample_dict :
    list66.append(sample_dict[k])
print(list66)
list66.sort()
print(list66[0])

#Change value of a key in a nested dictionary
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
dict8 = {"key1":2,"key2":1}
dict6 = {"key2":1,"key1":2}
print(dict8==dict6)

#we can get from a dictionary a list of keys and another one of values by using
print(dict.keys())
print(dict.values())
person = {"name": "Jessa", "country": "USA", "telephone": 1178}

for k in person :
    print(k,person[k])
#by using update method we can use more than one items
"""
"""
tuple1 = (10,20,30,40,50)
list6 = list(tuple1)
list6.reverse()
print(list6)
tuple2 = tuple(list6)
print(tuple2)

tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])
"""
"""
rows = 5
for i in range (rows):
    for j in range (0,i+1):
        print("*",end= " ")
    print()
for i in range(rows,1,-1):
    for j in range(i,1,-1):
        print("*", end=" ")
    print()
x = "hello world"

n = int(input("enter a positive  integer :"))  #enter an integer
sum = 0
for i in range (1,n):    #all numbers between 1 and n
    if n%i ==0:
        sum = sum + i  #sum all divisers of this number
if n == sum :
    print(n,"is a perfect integer ")  #check if it is perfect or not
"""
sent = input("enter a :")
n = len(sent)
i = 0
isalpha = 0
isalnum = 0
for i in range(0,n):
    if sent[i].isalpha()==True :
        isalpha = isalpha + 1
    elif sent[i].isalnum()==True:
        isalnum = isalnum +1
print(isalnum )
print(isalpha)