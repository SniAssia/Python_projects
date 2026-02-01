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
data = generate_random_database()
# q1 : number of members of each group
print(Display(data))
def mem_grp(grp):
    c=0
    for i in range(len(data['Group'])):
        if data['Group'][i]==grp:
            c+=1
    return c
for i in range(len(GROUPS)):
    print("number of members of grp", GROUPS[i], "is", mem_grp(GROUPS[i]))

# q2 : name of the student who has the lower minutes of delay
# in all sessions
