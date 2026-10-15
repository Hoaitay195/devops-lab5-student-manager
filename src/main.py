from student import Student

def main():
    students = [
        Student("SV001", "Nguyen Van A", 20, "K20"),
        Student("SV002", "Tran Thi B", 21, "K20"),
        Student("SV003", "Le Van C", 19, "K21")
    ]
    print("STUDENT MANAGER - DevOps Lab 5")
    for student in students:
        print(student)
    print(f"Total: {len(students)} students")

if __name__ == "__main__":
    main()

def search_student(students, keyword):
    return [
        s for s in students
        if keyword.lower() in s.name.lower()
        or keyword.lower() in s.student_id.lower()
    ]
