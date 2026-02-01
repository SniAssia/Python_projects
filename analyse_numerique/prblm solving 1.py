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
    {'Present': 1.0, 'Late': 0.95, 'Absent': 0.9},
    {'Present': 1.0, 'Late': 0.98, 'Very Late': 0.95, 'Absent': 0.93}
]

min_ATTENDANCE_RANGES = [
    {'Present': range(0,1,1), 'Late' : range(1,5,1), 'Absent': range(5,180,1)} ,
    {'Present': range(0,1,1), 'Late' : range(1,16,1), 'Absent': range(16,180,1)} ,
    {'Present': range(0,1,1), 'Late' : range(1,6,1), 'Very Late': range(6,10,1), 'Absent': range(10,180,1)} ,
    {'Present': range(0,1,1), 'Late' : range(1,10,1), 'Very Late': range(10,20,1), 'Absent': range(20,180,1)} ]

def generate_random_database():
    length = randint(6, 20)  # Number of students
    # Sample student names, assign genders and groups randomly
    students = sample(STUDENT_NAMES, length)
    genders = [choice(['M', 'F']) for _ in range(length)]
    groups = [choice(GROUPS) for _ in range(length)]
    # Generate random exam and TP scores
    exam_scores = np.random.randint(2, 21, size=(randint(1, 5), length)).tolist()
    tp_scores = np.random.choice([randint(8, 16), randint(10, 20), randint(16, 20)], size=(randint(2, 8), length)).tolist()
    # Random attendance records
    attendance = {day: [choice([randint(0, 30), 0]) for _ in range(length)] for day in sample(DAYS, randint(2, 4))}
    # Choose a random attendance option and generate min_att based on it
    dic_atd = choice(ATTENDANCE_OPTIONS)
    option_index = ATTENDANCE_OPTIONS.index(dic_atd)
    if option_index < len(min_ATTENDANCE_RANGES):
        min_att = min_ATTENDANCE_RANGES[option_index]
    else:
        # If there's no direct match (which shouldn't happen in this setup), default to the last available min_ATTENDANCE_RANGE
        min_att = min_ATTENDANCE_RANGES[-1]
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
        structured_data[day] = record
    return pd.DataFrame(structured_data)

data1 = generate_random_database()
#s refer to students
females = [s for s in data1['Student'] if data1['Gender'][data1['Student'].index(s)] == 'F']
print(females)


data2 = generate_random_database()
counter = {group: 0 for group in GROUPS} #creat a dict to count number of mem in each group
for student in data2['Student']:
    counter[data2['Group'][data2['Student'].index(student)]] += 1
# Find the group with the highest number of members
high_value = max(counter.values()) #we iterate over the dict created above to find the group with the highest number
high_group = [group for group, count in counter.items() if count == high_value][0]
print([high_group])

data3=generate_random_database()
high = 0
st = [] #students who has the highest minutes of delay in the last session
for i,j in zip(data3['Student'], data3['Attendance'].values()):
    ses = j[-1] #ses refer to last session
    if ses > high:
        high = ses
        st = [i]
    elif ses == high:
        st.append(i)
#display output
for i in st:
    print(i,end=",")
print()


data4 = generate_random_database()
dict = {k: 0 for k in data4['Student']} #k refer to student
for i , j in zip(data4['Student'], data4['Attendance'].values()):
    #we sum all sessions when the student was late
    late=0
    for session in i :
        late += 1
    dict[i] = late
print(dict)


data5 = generate_random_database()
for k in data5['Attendance']:
    dict={}
    for i in GROUPS:
        dict[i]=[]
        for j in range(len(data5['Student'])):
            st=data5['Student'][j] #st refer to students
            temp=data5['Attendance'][k][j]
            if data5['Group'][j]==i:
                if temp in data5['min_att']['Present']:
                    dict[i].append(1)
                elif temp in data5['min_att']['Late']:
                    dict[i].append(0.95)
                #elif temp in data5['min_att']['Very Late']:
                  #  dict[i].append(0.9)
                elif temp in data5['min_att']['Absent']:
                    dict[i].append(0.8)
high2=""
high=0


data6 = generate_random_database()
ses = {} #ses refer to sessions
for k in GROUPS:
    dela = {}
    min = float('inf')
    for i,j in data6['Attendance'].items():
        #enumerate function return tuple with item and their indexes
        for o, rec in enumerate(j):
            if data6['Group'][o] == k:
                if rec < min:
                    dela={'day':i}
                    min = rec
    ses[k] = dela
print(ses)

data7=generate_random_database()
max1=0
max2=list(data7['Attendance'].keys())[0]
for i in data7['Attendance']:
    dl=0
    for j in data7['Attendance'][i]:
        dl+=j
    if dl> max1:
        max1=j
        max2=i
average=max1/len(data7['Student'])
print(max2)
print(average)

data8=generate_random_database()
max1=data8['Group'][0]
max2=0
for i in GROUPS:
    if i in data7['Group']:
        average=0
        e=0
        for st in range(len(data7['Student'])):
            if data7['Group'][st]==i:
                e+=1
                for ex in data7['Exams']:
                    average+=ex[st]
        average/=e
        if average >max2:
            max1=i
            max2=average
print(max1)
dict={'F':0,'M':0}
for st in range(len(data7['Student'])):
    if data7['Group'][st]==max1:
        dict[data7['Gender'][st]]+=1
print(dict)



def mul_sum(x,l):
    t=0
    for i in l:
        if type(i)==list:
            t+=mul_sum(x,i)
        else:
            t+=x*i
    return t
data9 = generate_random_database()
min = {}
for i in GROUPS:
    grp = [data9['Attendance'][day] for day in data9['Attendance'] if i in data9['Group']]
    ttl = sum(sum(dy) for dy in grp)
    min[i] = {}
    for k,j in data9['min_att'].items():
        ttl2=0
        for o in range(len(j)):
            if len(grp)==0:
                break
            ttl2+=mul_sum(j[o],grp[o])
        min[i][k] = ttl2 / ttl if ttl != 0 else 0
print(min)


data4 = generate_random_database()
dict = {k: 0 for k in data4['Student']}
for i,j in data4['Attendance'].items():
    late= 0
    for session in i:
        if session > 0:
            late += 1
    dict[i] = late
print(dict)

