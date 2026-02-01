dict={}
x=dict.get('key') #we use it to get the value of a specific key
x=dict.keys() #we use it to get a list of all keys
x=dict.values() #we use it to get a list of all values
x=dict.items() #we use it to get every key and its value in one tuple including in a nested list
dict.update({"key":"value"}) #we use this method to update key and value in a dictionnary
dict.pop("key") #pop take as argument a key and its delete the key and its values
dict.popitem() #delete the last item
dict.clear() #the dict will become empty
for x,y in dict.items() :
    print(x,y)
newdict=dict.copy() #this method will help us to make changes in the old one
#these changes will not be executed on the new one
#second method
newdict=dict(dict)
