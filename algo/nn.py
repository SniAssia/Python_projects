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
    exam_scores = np.random.randint(2, 21, size=(randint(3, 8), length)).tolist()
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

#Q1
data=generate_random_database()
def transpose(l):
    new=[[0 for i in range(len(l))] for j in range(len(l[0]))]
    for i in range(len(l)):
        for j in range(len(l[i])):
            new[j][i]=l[i][j]
    return new
def cal_aver(l):
    mat=transpose(l)
    l0 = []
    for i in range(len(mat)):
        sum1=sum(mat[i])/len(mat[i])
        l0.append(sum1)
    return l0
l2=cal_aver(data['TPs'])
max_value= max(l2)
mx_index=[index for index,i in enumerate(l2) if i == max_value]
dict1={'Male':[],'Female':[]}
if len(mx_index)==1:
    print(data['Gender'][mx_index[0]])
else:
    for i in mx_index:
        if data['Gender'][i] =='Female' :
            dict1['Female'].append(data['Student'][i])
        elif  data['Gender'][i] =='Male' :
            dict1['Male'].append(data['Student'][i])
    print(dict1)


#Q2
l=[]
for i in data['Attendance']:
    l.append(i)
absent=[]
for i in range(len(data['Attendance'][l[0]])):
    if data['Attendance'][l[0]][i] in data['min_att']['Absent']:
        absent.append(data['Student'][i])
print(absent)


#Q3
exam1 = transpose(data['Exams'])
student =[]
for i in range(len(exam1)):
    if exam1[i][0:3]==sorted(exam1[i][0:3]):
        student.append(data['Student'][i])
print("students who have improved their marks are : ", student)


#Q4
tps=transpose(data['TPs'])
dict6={}
for i in range(len(tps)):
    if any(x >= 18 for x in tps[i]):
        dict6[data['Group'][i]] = [data['Student'][i]]
if len(dict6) == 1:
    print("student who have at least one tp score above 18 : ", dict6.keys())
else:
    print("students who have at least one tp score above 18 : ", dict6)


#Q5
l9=[]
for day in data['Attendance']:
    l9.append(data['Attendance'][day][1])
att = transpose(l9)
at=[]
for i in range(len(att)):
    sum1=sum(att[i])/len(att[i])
    at.append(sum1)
final = []
for i in range(len(at)):
    if at[i] in data['min_att']['Present'] and data['dic_atd']['Present'] >= 0.95:
        final.append(data['Student'][i])
    if 'Late' in data['min_att'] :
        if at[i] in data['min_att']['Late'] and data['dic_atd']['Late'] >= 0.95:
            final.append(data['Student'][i])
print(final)

#Q6
l1 = cal_aver(data['Exams']) # we use the function defined in the q1 to calculate the mean mark
print(l1)
dict8={x:[] for x in GROUPS}
for k in range(0,4):
    l=[]
    for i in range(len(l1)):
        if GROUPS[k]==data['Group'][i]:
            l.append(l1[i])
    mx_index=[index for index,x in enumerate(l) if x ==max(l)]
    for j in mx_index:
        if len(l) != 0:
            dict8[GROUPS[k]].append(data['Student'][l1.index(l[j])])
# print output
for i in dict8 :
    if len(dict8) == 1:
        dict8[i]= dict8[i][0]
    elif len(dict8[i])==0:
        del dict8[i]
print(dict8)


#Q7
def grp(group,var):
    c=0
    for i in range(len(data['Group'])):
        if data['Group'][i]==group and data['Gender'][i]==var:
            c+=1
    return c
dict_fem={x:0 for x in GROUPS}
fem=cal_aver(data['TPs'])
for k in range(0,4):
    for i in range(len(fem)):
        if GROUPS[k]==data['Group'][i] and data['Gender'][i]=='Female':
            dict_fem[GROUPS[k]] += fem[i]/grp(GROUPS[k],'Female')
# if the dictionary show the value 0
# this means that there is no female students in this grp or the mark obtained is 0
print("mean mark of tps marks for female students : " ,dict_fem)


#Q8
fem=cal_aver(data['TPs'])
dict_fem1={x:{'Male':0,'Female':0} for x in GROUPS}
for k in range(0,4):
    for i in range(len(fem)):
        if GROUPS[k]==data['Group'][i] and data['Gender'][i]=='Female':
            dict_fem1[GROUPS[k]]['Female'] += fem[i]/grp(GROUPS[k],'Female')
        elif GROUPS[k]==data['Group'][i] and data['Gender'][i]=='Male':
            dict_fem1[GROUPS[k]]['Male'] += fem[i]/grp(GROUPS[k],'Male')
print("mean mark of tps for each gender in the grp with the most students",dict_fem1)

#Q9
min_tp = {x: {'Female':0,'Male':0} for x in range(len(data['TPs']))}
for i in range(len(data['TPs'])):
    l=[]
    l1=[]
    for j in range(len(data['TPs'][i])):
        if data['Gender'][j]=='Male':
            l.append(data['TPs'][i][j])
        elif data['Gender'][j]=='Female':
            l1.append(data['TPs'][i][j])
    if len(l) != 0:
        min_tp[i]['Male']=min(l)
    if len(l1) != 0:
        min_tp[i]['Female'] = min(l1)
# this dict will display the minimum mark for each tp depending on gender
print(min_tp)

#Q10
average = {'Male':{x:0 for x in data['Student'] if data['Gender'][data['Student'].index(x)]=='Male' },'Female':{y:0 for y in data['Student'] if data['Gender'][data['Student'].index(y)]=='Female'}}
mat4=transpose(data['Exams'])
fnl=[]
for i in range(len(mat4)):
    sum1=sum(mat4[i])/len(mat4[i])
    fnl.append(sum1)
for i in range(len(fnl)):
    if data['Gender'][i]=='Male':
        average['Male'][data['Student'][i]]=fnl[i]
    elif data['Gender'][i]=='Female':
        average['Female'][data['Student'][i]]=fnl[i]
print(average)

#Q11
absent_st = {x:[] for x in data['Attendance']}
for day in data['Attendance']:
    for i in range(len(data['Attendance'][day][1])):
        if 'Absent' in data['min_att'] and data['Attendance'][day][1][i] in data['min_att']['Absent']:
            absent_st[day].append(data['Student'][i])
for i in absent_st:
    if len(absent_st[i])==1:
        absent_st[i]=str(absent_st[i][0])
    else :
        continue
print(absent_st)

#Q12

# we will use the list fnl defined in the previous question
print(fnl)


dict_male = {x: 0 for x in GROUPS}
for k in range(0,4):
    sum1=0
    for i in range(len(fnl)):
        if data['Gender'][i]=='Male' and data['Group'][i]==GROUPS[k]:
            sum1+=fnl[i]/grp(GROUPS[k],'Male')
    dict_male[GROUPS[k]]=sum1
print(dict_male)

#Q13
print(data['Exams'][-1])
last_exam=data['Exams'][-1]
dict_high={ x:[] for x in GROUPS}
for k in range(0, 4):
    l = []
    for i in range(len(last_exam)):
        if GROUPS[k]==data['Group'][i] :
            l.append(last_exam[i])
    if len(l) != 0:
        max_index=[index for index , x in enumerate(last_exam) if x==max(l)]
        for j in max_index:
            dict_high[GROUPS[k]].append(data['Student'][j])
# display output
for i in dict_high:
    if len(dict_high[i])==1:
        dict_high[i]=str(dict_high[i][0])
    else :
        continue
print(dict_high)

#Q14
def calculate_mean(l): # nested list
    mat=transpose(l)
    new_list=[]
    for i in range(len(mat)):
        sum1=sum(mat[i])/len(mat[i])
        new_list.append(sum1)
    return new_list
def calculate_median(l):
    l.sort()
    if len(l)%2==1:
        return l[len(l)//2]
    else :
        return (l[len(l)//2-1]+l[len(l)//2])/2


#Q16
absences = []
days = []
final_list = []
for day in data['Attendance']:
    days.append(day)
if 'Absent' in data['min_att'] :
    for day in data['Attendance']:
        counter = 0
        for i in range(len(data['Attendance'][day])):
            if data['Attendance'][day][i] in data['min_att']['Absent']:
                counter += 1
        absences.append(counter)
if len(absences) != 0:
    max_index=[index for index , x in enumerate(absences) if x ==max(absences)]
    for i in max_index :
        final_list.append(days[i])
if len(final_list)==1:
    print(str(final_list[0]))
else :
    print(final_list)


#Q17
days = []
for day in data['Attendance']:
    days.append(day)
max_l = []
for day in data['Attendance']:
    max_at = max(data['Attendance'][day][1])
    max_l.append(max_at)
final_l = []
max_index=[index for index , x in enumerate(max_l) if x==max(max_l)]
for j in max_index :
    final_l.append(days[j])
if len(final_l)==1:
    print(str(final_l[0]))
else :
    print(final_l)


#Q18
def grp1(group):
    c=0
    for i in range(len(data['Group'])):
        if data['Group'][i]==group :
            c+=1
    return c
final_aver = []
for i in range(len(data['Exams'])):
    aver=[]
    for k in range (0, 4):
        s=0
        for j in range(len(data['Exams'][i])):
            if data['Group'][j] == GROUPS[k]:
                s += data['Exams'][i][j]/grp1(GROUPS[k])
        aver.append(s)
    final_aver.append(aver)
new_exam=transpose(data['Exams'])
dict_count = {}
for i in range(len(new_exam)):
    counter = 0
    for k in range(0, 4):
        for j in range(len(new_exam[i])):
            if data['Group'][i]==GROUPS[k] :
                if new_exam[i][j] >= final_aver[j][k]:
                    counter += 1
    dict_count[data['Student'][i]]=counter
print(dict_count)




#Q19
def grp2(var):
    c=0
    for i in range(len(data['Gender'])):
        if data['Gender'][i]==var :
            c+=1
    return c
aver_delay = {x :  {'Male':0,'Female':0} for x in data['Attendance']}
for day in data['Attendance']:
    aver=0
    aver1=0
    for i in range(len(data['Attendance'][day][1])):
        if data['Gender'][i] == 'Male' :
            aver += data['Attendance'][day][1][i]/grp2('Male')
        elif data['Gender'][i] == 'Female' :
            aver1 += data['Attendance'][day][1][i]/grp2('Female')
    aver_delay[day]['Male'] = aver
    aver_delay[day]['Female'] = aver1
print('the average delay across every session is : ',aver_delay)

#Q20
tp_score = transpose(data['TPs'])
tp_score_list = []
empty_dict = {'Male':0,'Female':0}
for i in range(len(tp_score)):
    sum1=sum(tp_score[i])/len(tp_score[i])
    tp_score_list.append(sum1)
c1 = 0
c2 = 0
for i in range(len(tp_score_list)):
    if data['Gender'][i] == 'Male' and tp_score_list[i] >= 12 :
        c1 += 1
    if data['Gender'][i] == 'Female' and tp_score_list[i] >= 12 :
        c2 += 1
empty_dict['Male']=c1
empty_dict['Female']=c2
print(empty_dict)

