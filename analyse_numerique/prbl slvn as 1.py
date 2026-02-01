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
data=generate_random_database()
# q1 : names of the female students
for i in range(len(data['Student'])):
    if data['Gender'][i]=='F':
        print(data['Student'][i])

# q2 : names of the groups that have the highest number of members
dict={x : 0 for x in GROUPS}
for i in range(len(data['Student'])):
    dict[data['Group'][i]]+=1
max1=max(dict.values())
list=[x for x,y in dict.items() if y ==max1]
print(list)


# q3 : name of student that have the highest minutes
# of delay in the last session
l=[]
for i in data['Attendance'].values():
    l.append(i)
l1 = l[-1]
pivot=l1[0]
for i in range(len(l1)):
    if l1[i]>pivot:
        pivot=l1[i]
print(data['Student'][l1.index(pivot)])


# q4 : for each student, print the count of sessions they were late
# output : dict
dict1={}
mat=[[0 for i in range(len(l))] for j in range(len(l[0]))]
for i in range(len(l)):
    for j in range(len(l[i])):
        mat[j][i]=l[i][j]
for i in range(len(mat)):
    count =0
    for j in range(len(mat[i])):
        if mat[i][j] in data['min_att']['Late']:
            count+=1
    dict1[data['Student'][i]]=count
print(dict1)
# q5 : print the group with the highest average attendance
# rate for each session
dict2={}
def grp(group):
    c=0
    for i in range(len(data['Group'])):
        if data['Group'][i]==group:
            c+=1
        else :
            continue
    return c
print(Display(data))
for day in data['Attendance']:
    l1=[]
    for k in range(0,4):
        c=0
        for i in range(len(data['Attendance'][day])):
            if data['Attendance'][day][i] in data['min_att']['Present'] and GROUPS[k]==data['Group'][i]:
                c += data['dic_atd']['Present']/grp(data['Group'][i])
            elif data['Attendance'][day][i] in data['min_att']['Late'] and GROUPS[k]==data['Group'][i]:
                c += data['dic_atd']['Late']/grp(data['Group'][i])
            if 'very_late ' in data['min_att']:
                if data['Attendance'][day][i] in data['min_att']['Very Late'] and GROUPS[k]==data['Group'][i]:
                    c += data['dic_atd']['Very Late'] / grp(data['Group'][i])
            else :
                continue
            if 'Absent' in data['min_att']:
                if data['Attendance'][day][i] in data['min_att']['Absent'] and GROUPS[k]==data['Group'][i]:
                    c += data['dic_atd']['Absent '] / grp(data['Group'][i])
            else :
                continue
        l1.append(c)
    print("the grp with the highest average attendance for ",day,"is: ", GROUPS[l1.index(max(l1))])


# q6 : print the session for each grp with less delay in minutes
l3=[]
for day in data['Attendance']:
    l3.append(day)
dict3 = {}
for k in range(0, 4):
    l = []
    for day in data['Attendance']:
        c = 0
        for i in range(len(data['Attendance'][day])):
            if GROUPS[k] == data['Group'][i]:
                c += data['Attendance'][day][i]/grp(data['Group'][i])
        l.append(c)
        dict3[GROUPS[k]]=l3[l.index(min(l))]
print(dict3)


# q7 : identify the session with the highest delay and print its average delay
# time
l2=[]
for day in data['Attendance']:
    l2.append(day)
l = []
for day in data['Attendance']:
    sum1 = sum(data['Attendance'][day])
    l.append(sum1)
print("the session with the highest delay is : ",l2[l.index(max(l))])
print("its average delay time is : ",max(l)/len(data['Student']))

# q8 : the gender distribution in the group with the highest average exam
# score
dict4 = {}
lf = []
lm = []
for k in range(0,4):
    cf = 0
    cm = 0
    for i in range(len(data['Student'])):
        if data['Gender'][i]=='F' and GROUPS[k]==data['Group'][i]:
            cf += 1
        if data['Gender'][i]=='M' and GROUPS[k]==data['Group'][i]:
            cm += 1
    lf.append(cf)
    lm.append(cm)
print("the gender distribution for each grp is : ")
print(lf)
print(lm)
for i in range(len(data['Exams'])):
    print(data['Exams'][i])
mat = [[0 for i in range(len(data['Exams']))] for j in range(len(data['Exams'][0]))]
for i in range(len(data['Exams'])):
    for j in range(len(data['Exams'][i])):
        mat[j][i]=data['Exams'][i][j]
l = []
for i in range(len(mat)):
    sum1 = sum(mat[i])/len(mat[i])
    l.append(sum1)
print(l)
l0 = []
for k in range(0, 4):
    s1 = 0
    for i in range(len(l)):
        if data['Group'][i] == GROUPS[k]:
            s1 += l[i] / grp(data['Group'][i])
    l0.append(s1)
print("the grp with the highest average exam score is ", GROUPS[l0.index(max(l0))])
# the gender distribution in this grp
cf = 0
cm = 0
for i in range(len(data['Group'])):
    if data['Group'][i] == GROUPS[l0.index(max(l0))] and data['Gender'][i]=='F':
        cf += 1
    elif data['Group'][i] == GROUPS[l0.index(max(l0))] and data['Gender'][i]=='M':
        cm += 1
print('the gender distribution in this grp is : ')
print('for males ', cm)
print('for females : ', cf)

# q9 : for each grp , print the minimum mark on the exams

for i in range(len(data['Exams'])):
    for k in range(0, 4):
        l12 = []
        for j in range(len(data['Exams'][i])):
                if GROUPS[k] == data['Group'][j] :
                    l12.append(data['Exams'][i][j])
        if len(l12) != 0:
            print('the minimum mark for ',GROUPS[k],"on the exam ",i,"is",min(l12))

# q10 : the final mark based on this formula
# calculate mean of exams:
exams = []
for i in range(len(mat)):
    sum1=sum(mat[i])/len(mat[i])
    exams.append(sum1)
print("exams",exams)
tps = []
mat2=[[0 for i in range(len(data['TPs']))] for j in range(len(data['TPs'][0]))]
for i in range(len(data['TPs'])):
    for j in range(len(data['TPs'][i])):
        mat2[j][i]=data['TPs'][i][j]
for i in range(len(mat2)):
    sum1=sum(mat2[i])/len(mat2[i])
    tps.append(sum1)
print("tps: ",tps)


l6=[]
for day in data['Attendance']:
    l6.append(data['Attendance'][day])
mat3=[[0 for i in range(len(l6))] for j in range(len(l6[0]))]
for i in range(len(l6)):
    for j in range(len(l6[i])):
        mat3[j][i]=l6[i][j]
rate=[]
for i,j,k in zip(exams,tps,rate):
    final=(i*0.6+j*0.4)*k
    print("final marks for students are : ",final)
# q11 :
#mat
# the first semester
print("these : ")
for i in range(len(mat)):
    print(mat[i])
l23 = []
for i in range(len(mat)):
    n = (len(mat[0]) - 1) / 2
    m = len(mat[0]) / 2
    sum1=0
    if type(n)==int:
        for j in range(0, int(n)):
            sum1+=mat[i][j]/int(n)
    else :
        for j in range(0, int(m)):
            sum1+=mat[i][j]/int(m)
    l23.append(sum1)
print("the first semester", l23)
# the second semester
if len(mat[0])>1:
    l2 = []
    for i in range(len(mat)):
        n = (len(mat[0]) - 1) / 2
        m = len(mat[0]) / 2
        sum1=0
        if type(n)==int:
            for j in range(int(n),len(mat[i])):
                sum1+=mat[i][j]/int(n)
        else :
            for j in range(int(m), len(mat[i])):
                sum1+=mat[i][j]/int(m)
        l2.append(sum1)
    print("the second semester ",l2)
    for i, j in zip(l23,l2):
        if (i+0.1*i) <= j:
            print(data['Student'][l23.index(i)])
else :
    print("there is just one exam ")

