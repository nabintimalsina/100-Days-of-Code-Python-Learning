student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grade = {}
for key, value in student_scores.items():
    if value in range(91, 101):
        student_grade[key] = "Outstanding"
    elif value in range(81, 91):
        student_grade[key] = "Exceeds Expectations"
    elif value in range(71, 81):
        student_grade[key] = "Acceptable"
    else:
        student_grade[key] = "Fail"

print(f"Student Grades: {student_grade} \n")