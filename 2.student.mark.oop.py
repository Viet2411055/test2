# 1.student.mark.py
# Copy 2
def input_number_students():
    while True:
        try:
            n = int(input("Enter number of students: "))
            if n > 0:
                return n
            print("Number must be positive.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def input_student_info():
    students = []
    n = input_number_students()
    for _ in range(n):
        while True:
            sid = input("Enter student ID: ").strip()
            if sid and all(sid != s[0] for s in students):
                break
            print("Invalid or duplicate student ID.")
        name = input("Enter student name: ").strip()
        dob = input("Enter student DoB (YYYY-MM-DD): ").strip()
        students.append((sid, name, dob))
    return students

def input_number_courses():
    while True:
        try:
            n = int(input("Enter number of courses: "))
            if n > 0:
                return n
            print("Number must be positive.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def input_course_info():
    courses = []
    n = input_number_courses()
    for _ in range(n):
        while True:
            cid = input("Enter course ID: ").strip()
            if cid and all(cid != c[0] for c in courses):
                break
            print("Invalid or duplicate course ID.")
        name = input("Enter course name: ").strip()
        courses.append((cid, name))
    return courses

def select_course(courses):
    print("\nAvailable courses:")
    for i, (cid, cname) in enumerate(courses, 1):
        print(f"{i}. {cid} - {cname}")
    while True:
        try:
            choice = int(input("Select a course by number: "))
            if 1 <= choice <= len(courses):
                return courses[choice-1][0]
            print("Choice out of range.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def input_marks(students, course_id, marks_dict):
    print(f"\nInputting marks for course {course_id}")
    for sid, name, _ in students:
        while True:
            try:
                mark = float(input(f"Enter mark for student {name} (ID: {sid}): "))
                if 0 <= mark <= 100:
                    marks_dict.setdefault(course_id, {})[sid] = mark
                    break
                print("Mark must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

def list_courses(courses):
    print("\nCourses:")
    for cid, cname in courses:
        print(f"{cid} - {cname}")

def list_students(students):
    print("\nStudents:")
    for sid, name, dob in students:
        print(f"ID: {sid}, Name: {name}, DoB: {dob}")

def show_marks_for_course(course_id, students, marks_dict):
    print(f"\nMarks for course {course_id}:")
    if course_id not in marks_dict:
        print("No marks entered yet for this course.")
        return
    course_marks = marks_dict[course_id]
    for sid, name, _ in students:
        mark = course_marks.get(sid, "N/A")
        print(f"Student {name} (ID: {sid}): {mark}")

def main():
    students = []
    courses = []
    marks_dict = {}  # {course_id: {student_id: mark}}

    while True:
        print("\nStudent Mark Management System")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks for a course")
        print("4. List courses")
        print("5. List students")
        print("6. Show marks for a course")
        print("7. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            students = input_student_info()
        elif choice == '2':
            courses = input_course_info()
        elif choice == '3':
            if not students or not courses:
                print("You need to input students and courses first.")
                continue
            cid = select_course(courses)
            input_marks(students, cid, marks_dict)
        elif choice == '4':
            if not courses:
                print("No courses to show.")
            else:
                list_courses(courses)
        elif choice == '5':
            if not students:
                print("No students to show.")
            else:
                list_students(students)
        elif choice == '6':
            if not courses:
                print("No courses available.")
                continue
            cid = select_course(courses)
            if not students:
                print("No students available.")
                continue
            show_marks_for_course(cid, students, marks_dict)
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
