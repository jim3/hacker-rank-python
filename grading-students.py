# ---------------------------------------#
# ----------grading_students.py----------#
# ---------------------------------------#
import math


def gradingStudents(grades):
    for i in range(len(grades)):
        if (grades[i] >= 38):
            r_num = math.ceil(grades[i] / 5) * 5
            if (r_num - grades[i] < 3):
                grades[i] = r_num
    return grades


grades = [73, 67, 84, 38, 33, 40]
result = gradingStudents(grades)
print(result)

