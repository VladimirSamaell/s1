grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
def calculate_grades(grades):
    return sum(grades) / len(grades)
def map_students_average(students, grades):
    students_sorted = sorted(students)
    gpa = {students: calculate_grades(grades[i]) for i, students in enumerate(students_sorted)}
    return gpa
gpa = map_students_average(students, grades)
print(gpa)