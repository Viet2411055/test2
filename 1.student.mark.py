# 1.student.mark.py

def input_number(msg):
    return int(input(msg))

def input_students():
    students = []
    n = input_number("Number of students: ")
    for _ in range(n):
        sid = input("Student ID: ")
        name = input("Name: ")
        dob = input("DoB: ")
        students.append((sid, name, dob))
    return students

def input_courses():
    courses = []
    n = input_number("Number of courses: ")
    for _ in range(n):
        cid = input("Course ID: ")
        cname = input("Course name: ")
        courses.append((cid, cname))
    return courses

def select_course(courses):
    for i, (cid, cname) in enumerate(courses, 1):
        print(f"{i}. {cid} - {cname}")
    choice = int(input("Select course number: "))
    return courses[choice-1][0]

def input_marks(students, course_id, marks):
    marks[course_id] = {}
    for sid, name, dob in students:
        mark = float(input(f"Mark for {name}: "))
        marks[course_id][sid] = mark

def list_courses(courses):
    print("\nCourses:")
    for cid, cname in courses:
        print(f"{cid} - {cname}")

def list_students(students):
    print("\nStudents:")
    for sid, name, dob in students:
        print(f"{sid} - {name} - {dob}")

def show_marks(course_id, students, marks):
    print(f"\nMarks for course {course_id}:")
    if course_id not in marks:
        print("No marks for this course.")
        return
    for sid, name, dob in students:
        mark = marks[course_id].get(sid, "N/A")
        print(f"{name}: {mark}")

def main():
    students = input_students()
    courses = input_courses()
    list_courses(courses)
    list_students(students)
    c_id = select_course(courses)
    marks = {}
    input_marks(students, c_id, marks)
    show_marks(c_id, students, marks)


if __name__ == "__main__":
    main()
