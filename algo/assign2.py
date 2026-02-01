from random import randint, sample, choice
import numpy as np
import pandas as pd

# Define constants for ease of modification and readability
STUDENT_NAMES = [
    "Mohammed", "Fatima", "Ahmed", "Amina", "Hassan", "Nora", "Youssef", "Laila",
    "Abdel", "Sanaa", "Karim", "Houda", "Omar", "Meryem", "Ali", "Salma",
    "Saad", "Imane", "Rachid", "Kawtar", "Jamal", "Soukaina", "Fouad", "Farah",
    "Mustapha", "Hanan", "Adil", "Zineb", "Tariq", "Rania", "Sofia", "Khalid",
    "Asmaa", "Anas", "Najat", "Bilal", "Samira", "Ayoub", "Malika", "Yassine"
]
GROUPS = ['A', 'B', 'C', 'D']
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
ATTENDANCE_OPTIONS = [
    {'Present': 1.0, 'Late': 0.95, 'Very Late': 0.9, 'Absent': 0.8},
    {'Present': 1.0, 'Absent': 0.9},
    {'Present': 1.0, 'Late': 0.9, 'Very Late': 0.75, 'Absent': 0.5},
    {'Present': 1.0, 'Absent': 0.8},
    {'Present': 1.0, 'Late': 0.98, 'Very Late': 0.95, 'Absent': 0.93}
]


def generate_random_database():
    length = randint(6, 20)  # Number of students

    # Sample student names, assign genders and groups randomly
    students = sample(STUDENT_NAMES, length)
    genders = [choice(['Male', 'Female']) for _ in range(length)]
    groups = [choice(GROUPS) for _ in range(length)]

    # Generate random exam and TP scores
    exam_scores = np.random.randint(2, 21, size=(randint(1, 5), length)).tolist()
    tp_scores = np.random.choice([randint(8, 16), randint(10, 20), randint(16, 20)], size=(randint(3, 8), length)).tolist()

    # Random attendance records
    attendance = {}
    for day in sample(DAYS, randint(2, 4)):
        attendance[day] = [np.random.choice([60,90,120,150,180])]+[[choice([randint(0, 30), 0]) for _ in range(length)]]


    # Choose a random attendance option and generate min_att based on it
    dic_atd = choice(ATTENDANCE_OPTIONS)
    min_att = {}
    start_point = 0  # Starting point for the first range

    for key in dic_atd.keys():
        end_point = start_point + np.random.randint(1, 10)  # Generate end point
        min_att[key] = range(start_point, end_point)
        start_point = end_point  # Update start for the next range to be continuous

    min_att["Absent"] = range(min_att["Absent"][0], 180)

    # Construct and return the database as a pandas DataFrame
    data = {
        'Student'    : students,
        'Gender'     : genders,
        'Group'      : groups,
        "Exams"      : [score for i, score in enumerate(exam_scores)],
        "TPs"        : [score for i, score in enumerate(tp_scores)],
        "Attendance" : attendance,
        "dic_atd" : dic_atd,
        "min_att" : min_att,
    }
    return data
def Display(data_dictionary):
    # Preparing structured data for DataFrame
    structured_data = {'Student': data_dictionary['Student'], 'Gender': data_dictionary['Gender'], 'Group': data_dictionary['Group']}
    for i in range(len(data_dictionary['Exams'])):
        structured_data[f'Exam_{i+1}'] = data_dictionary['Exams'][i]
    for i in range(len(data_dictionary['TPs'])):
        structured_data[f'TP_{i+1}'] = data_dictionary['TPs'][i]
    for day, record in data_dictionary['Attendance'].items():
        structured_data[day] = record[1]
    return pd.DataFrame(structured_data)
"""
data1=generate_random_database()
dict1={}
for i in data1['Group']:
    if i not in dict1:
        dict1[i]=0
    dict1[i]+=1
print(dict1)
grp=Display(data1) #this function display all data that we have
print(grp)

data2=generate_random_database()
l=None #this variable will take noun of student that have the lower minutes
min=float('inf')
for i in data2['Student']:
    count=0
    for j in data2['Attendance']:
        minutes=data2['Attendance'][j][1][data2['Student'].index(i)]
        count+=minutes
    if count<min:
        min=count
        l=i
print(l)
print(Display(data2))


data3=generate_random_database()
dict={}
for i in data2['Student']:
    if data2['Gender'][data2['Student'].index(i)]=='Female':
        if data2['Group'][data2['Student'].index(i)] not in dict:
            dict[data2['Group'][data2['Student'].index(i)]]=1
        else :
            dict[data2['Group'][data2['Student'].index(i)]] +=1
l4=[]
for i in dict.values():
    l4.append(i)
min1=min(l4)
#this list will contain just groups that have fewest females
less=[i for i,j in dict.items() if j==min1]
#display the output as a dict
dict1={}
for i in less:
    l3=[j for j in data2['Student'] if data2['Group'][data2['Student'].index(j)]==i]
    dict1[i]=l3
print(dict1)
"""
"""
data2=generate_random_database()
list=[]
for i in range(len(data2["Student"])):
    point=0
    #put a variable to check attendance
    att=0
    for j in range(len(data2["TPs"])):
        #check if it is high than 14 or not
        if data2["TPs"][j][i]>14:
            point+=1
    for k in data2["Attendance"]:
        for o in data2["min_att"]:
            if data2["Attendance"][k][1][i] in data2["min_att"][o]:
                att+=data2["dic_atd"][o]
    #then we calculate the average
    att=att/len(data2["Attendance"])
    #check if they contain the same number of elements and the attendance satisfy the condtion
    if point==len(data2["TPs"]) and att>0.96:
        list.append(data2["Student"][i])
#we print the output
if len(list)==1:
    print(list[0])
else:
    for i in list:
        print(i,end=",")

data2=generate_random_database()
l1=[]
for i in data2["Group"]:
    if i not in l1:
        #we append groups to this list
        l1.append(i)
#we create a dict where we will append the final output
dict3={j:0 for j in l1}
for j in dict3:
    l3=[]
    for k in range(len(data2["Student"])):
        if data2["Group"][k]==j:
            l3.append(k)
    point=0

    for o in l3:
        for k in range(len(data2["TPs"])):
            #we calculate the marks obtained in tp
            point+=data2["TPs"][k][o]
    #we calculate the average
    dict3[j]=point/(len(data2["TPs"])*len(l3))
#we print the final output
print(dict3)


list=[]
if len(data2["Exams"])==1:
    print(list)
else:
    for st_index in range(len(data2["Student"])):
        #we check if every mark is higher than the previous exam for rvery student
        if all(data2["Exams"][ex_index][st_index]<data2["Exams"][ex_index+1][st_index] for ex_index in range(len(data2["Exams"])-1)):
            list.append(data2["Student"][st_index])
    print(list) #display the output
"""

data2=generate_random_database()

dict={'Female':[],'Male':[]}
dict2={'Female':21,'Male':21} #21 refer to the high mark that we can have
for i in data2['Exams']:
    for j in range(len(data2['Student'])):
        if i[j]<dict2[data2['Gender'][j]]:
            #the lower value will become this value that we check recently
            dict2[data2['Gender'][j]]=i[j]
for i in data2['Exams']:
    for j in range(len(data2['Student'])):
        if i[j]==dict2[data2['Gender'][j]]:
            if data2['Student'][j] not in dict[data2['Gender'][j]]:
                dict[data2['Gender'][j]].append(data2['Student'][j])
print(dict)


#q7
#initialize dictionnaries
att={i:0 for i in GROUPS if i in data2['Group']}
eff={i:0 for i in GROUPS if i in data2['Group']}
for i in range(len(data2['Student'])):
    eff[data2['Group'][i]]+=1
    count=0
    for j in data2['Attendance']:
        for k in data2['min_att']:
            if data2['Attendance'][j][1][i] in data2['min_att'][k]:
                #counter add attendance rate
                count+=data2['dic_atd'][k]
    #we calculate the average
    count=count/len(data2['Attendance'])
    #we add to the dict their values
    att[data2['Group'][i]]+=count
for i in att:
    att[i]/=eff[i]
print(att)

data2 = generate_random_database()
dict = {}
#dict will contain days and (duration of seesion - delay)
for i,j in data2['Attendance'].items():
    dict[i] = sum([j[0] - del1 if del1 < j[0] else 0 for del1 in j[1]])
    #del1 refer to delay
print(dict)


data2 = generate_random_database()
tp=[]
for i in range(len(data2['Student'])):
    for j in range(len(data2['TPs'])-2):
        if data2['TPs'][j][i]<data2['TPs'][j+1][i]<data2['TPs'][j+2][i]:
            tp.append(data2['Student'][i])
            break
print(tp)


dict = {j: sum([int(i) for i in k[1] if type(i)==int]) for j,k in zip(data2['Student'], data2['Attendance'])}
#take the high value from this dict
max1 = max(dict.values())
#this list refer to students name with the highest attendance
st = [i for i,j in dict.items() if j == max1]
#print output as a list
print(st)
