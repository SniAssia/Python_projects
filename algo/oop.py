"""
class person():
    def __init__(self,name,country,birth,year):
        self.name =name
        self.country=country
        self.birth=birth
        self.year=year
    def getbirth(self):
        return self.year-self.birth
name = input("enter ur name : ")
country =input("enter your country : ")
birth = int(input("enter your date of birth : "))
year = int(input("enter the current year : "))
obj=person(name,country,birth,year)
print(obj.getbirth())
print(obj.name)
print(obj.country)


#use class to create a calculator
class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a-self.b
    def div(self):
        return self.a/self.b
    def mul(self):
        return self.a*self.b
a=int(input())
b=int(input())
obj= cal(a,b)
choice =1
while choice !=0:
    print("1:addition")
    print("2:multiplication")
    print("3:division")
    print("4:sub")
    choice = int(input())
    if choice ==1:
        print(obj.add())
    elif choice ==2:
        print(obj.sub())
class shop():
    def __init__(self):
        self.items = {}
    def add(self,item_name_to_add,price):
        self.items[item_name_to_add]=price
        return self.items
    def remove(self,item_name_to_remove):
        for i in self.items :
            if i==item_name_to_remove:
                del self.items[i]
        return self.items
    def total(self):
        total = 0
        for  i in self.items :
            total +=self.items[i]
        return total
obj = shop()
print(obj.add("orange",100))
print(obj.add("pink",120))
print(obj.add("eee",120))
print(obj.total())

class list():
    def __init__(self):
        self.e=[]
    def push(self,a):
        self.e.append(a)
        return self.e
    def pop(self):
        self.e.remove(self.e[-1])
        return self.e
obj=list()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)

obj.push(50)
obj.push(60)
obj.push(70)
print(obj.push(80))


#manage a bank
class bank():
    def __init__(self):
        self.customers={}
    def createaccount(self,number,money):
        self.customers[number]=money
        return self.customers
    def add(self,number,newbalance):
        for i in self.customers:
            if i == number :
                self.customers[number]+=newbalance
    def remove(self,number,amountremoved):
        for i in self.customers :
            if i == number :
                if self.customers[number]>=amountremoved:
                    self.customers[number]-=amountremoved
                    print("withdrawal successful")
                else :
                    print("you can't do this operation ")
            else :
                print("this account doesn't exist ")
    def displaybalance(self):
        for i in self.customers:
            print("your actual balance is : ",self.customers[i])
obj = bank()
print(obj.createaccount("H-1298",123))
print(obj.createaccount("A-1298",166))
print(obj.createaccount("B-1298",12321))
print(obj.createaccount("C-1298",3456))
print(obj.createaccount("D-1298",178))
print(obj.createaccount("E-1298",198))
print(obj.createaccount("F-1298",167))
print(obj.createaccount("G-1298",109))
print(obj.add("H-1298",123))
"""
#create a class with instance attributes
class vehicule():
    def __init__(self,maxspeed,mileage):
        self.maxspeed=maxspeed
        self.mileage=mileage
obj= vehicule(240,18)
print(obj.maxspeed)
print(obj.mileage)
class child():
    def init(self,name,maxspeed,mileage):
        self.name=name
        self.maxspeed=maxspeed
        self.mileage=mileage

# Base class
class Vehicule():

    def __init__(self, name, color, price):
        self.name = name
        self.color=color
        self.price=price
    def info(self):
        print(self.color,self.price,self.name)
class car(Vehicule):
    def info2(self,no):
        print(self.name ,no)
obj=car("bbb","black",88)
obj.info()
obj.info2(5)


def convert_temp(input_temp, input_unit):
    if input_unit.lower() == 'f':
        output_temp = (input_temp - 32) * 5 / 9
        output_unit = '°C'
    elif input_unit.lower() == 'c':
        output_temp = (input_temp * 9 / 5) + 32
        output_unit = '°F'
    else:
        return "Invalid input unit. Please enter 'F' for Fahrenheit or 'C' for Celsius."

    return f"{output_temp} {output_unit}"


input_temp = float(input("Enter the temperature: "))
input_unit = input("Enter the unit of temperature (F or C): ")

result = convert_temp(input_temp, input_unit)
print(result)


