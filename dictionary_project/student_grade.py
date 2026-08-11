#Prgram to convert student scores into grades using a python dictionary.
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grade = {}
for key, value in student_scores.items():
    #Function: .items() is a special dictionary tool. Instead of just giving you the keys (names),
    #  it gives you the key AND the value bundled together.
    #Python opens the student_scores dictionary, grabs the very first pair ("Harry", 88), 
    # puts "Harry" in the key box, puts 88 in the value box, and steps inside the loop.
    print(f"Student: {key}, Score: {value}")
    if value in range(91, 101):
        student_grade[key] = "Outstanding"
    elif value in range(81, 91):
        student_grade[key] = "Exceeds Expectations"
    elif value in range(71, 81):
        student_grade[key] = "Acceptable"
    else:
        student_grade[key] = "Fail"

print(f"Student Grades \n: {student_grade} ")



