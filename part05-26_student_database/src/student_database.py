# Write your solution here
def add_student(students: dict, name: str):
    students[name] = []


def is_no_matching_course_or_lower_grade(student: list[tuple[str, int]], course_info: tuple[str, int]):
    matches_ = [
        course_info[0] == course_info_[0] and course_info[1] < course_info_[1]
        for course_info_ in student
    ]
    return len(matches_) == 0 or not any(matches_)


def add_course(students: dict, name: str, course_info: tuple[str, int]):
    if name not in students:
        print(f"{name}: no such person in the database")
        return

    student = students[name]

    if course_info[1] > 0:

        if len(student) == 0 or (
                is_no_matching_course_or_lower_grade(student, course_info)
        ):
            student.append(course_info)

        if sum([name == course_info[0] for name, grade in student]) > 1:
            max_grade = max(student, key=lambda x: x[1])[1]
            for course, grade in student:
                if grade < max_grade:
                    student.remove((course, grade))


def get_gpa(student: list[tuple[str, int]]) -> float:
    return sum([course_grade[1] for course_grade in student]) / len(student)


def print_student(students: dict, name: str):
    if name not in students:
        print(f"{name}: no such person in the database")
        return
    else:
        print(f"{name}: ")
        if len(students[name]) == 0:
            print(f" no completed courses")
            return
        else:
            print(f" {len(students[name])} completed courses:")
            grades = []
            for course_name, grade in students[name]:
                print(f"  {course_name} {grade}")
                grades.append(grade)
            print(f" average grade {sum(grades) / len(grades):.1f}")


def summary(students):
    print(f"students {len(students)}")

    student_w_most_courses = max(students, key=lambda x: len(students[x]))
    most_courses = len(students[student_w_most_courses])

    student_w_best_gpa = max(students, key=lambda x: get_gpa(students[x]))
    best_gpa = get_gpa(students[student_w_best_gpa])

    print(f"most courses completed {most_courses} {student_w_most_courses}")
    print(f"best average grade {best_gpa:.1f} {student_w_best_gpa}")


if __name__ == "__main__":
    students_ = {}
    add_student(students_, "Peter")
    add_student(students_, "Eliza")
    print_student(students_, "Peter")
    print_student(students_, "Eliza")
    print_student(students_, "Jack")

    students_ = {}
    add_student(students_, "Peter")
    add_course(students_, "Peter", ("Introduction to Programming", 3))
    add_course(students_, "Peter", ("Advanced Course in Programming", 2))
    print_student(students_, "Peter")

    students_ = {}
    add_student(students_, "Peter")
    add_course(students_, "Peter", ("Introduction to Programming", 3))
    add_course(students_, "Peter", ("Advanced Course in Programming", 2))
    add_course(students_, "Peter", ("Data Structures and Algorithms", 0))
    add_course(students_, "Peter", ("Introduction to Programming", 2))
    add_course(students_, "Peter", ("Introduction to Programming", 5))
    print_student(students_, "Peter")

    students_ = {}
    add_student(students_, "Peter")
    add_student(students_, "Eliza")
    add_course(students_, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students_, "Peter", ("Introduction to Programming", 1))
    add_course(students_, "Peter", ("Advanced Course in Programming", 1))
    add_course(students_, "Eliza", ("Introduction to Programming", 5))
    add_course(students_, "Eliza", ("Introduction to Computer Science", 4))
    summary(students_)
