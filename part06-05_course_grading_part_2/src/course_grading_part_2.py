# write your solution here
import os
import math
from typing import Type


mapping = (
    ((0, 14), 0),
    ((15, 17), 1),
    ((18, 20), 2),
    ((21, 23), 3),
    ((24, 27), 4),
    ((28, 40), 5)
)


def get_grade(n_points: int) -> int:
    for score_range, grade_value in mapping:
        if score_range[0] <= n_points <= score_range[1]:
            return grade_value
    raise ValueError(f"Illegal number of points : {n_points}!")


def read_csv(path: str, type_cast: Type[str] | Type[int]) -> list[dict[str, str | int]]:
    with open(path, "r") as f:
        lines = f.readlines()
    header = [h.strip() for h in lines[0].split(";")]
    data = []
    for line in lines[1:]:
        data.append(
            {key: type_cast(value) if key != "id" else int(value) for key, value in zip(header, [l.strip() for l in line.split(";")])}
        )
    return data


def get_points_sum(datum) -> int:
    return sum(datum[col] for col in list(datum.keys())[1:])


def get_data_by_id(data: list[dict[str, str | int]], datum_id: int) -> list[dict[str, str | int]]:
    return [datum for datum in data if datum["id"] == datum_id]


def get_path(filename: str) -> str:
    path_: str = os.path.join(os.path.dirname(__file__), filename)
    return path_


student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")

# student_info_ = read_csv(get_path(student_info), str)
# exercise_data_ = read_csv(get_path(exercise_data), int)
# exam_points_ = read_csv(get_path(exam_points), int)

student_info_ = read_csv(student_info, str)
exercise_data_ = read_csv(exercise_data, int)
exam_points_ = read_csv(exam_points, int)

for student in student_info_:

    name = f"{student['first']} {student['last']}"

    exercises = get_data_by_id(exercise_data_, student['id'])
    exam = get_data_by_id(exam_points_, student['id'])

    if len(exercises) == 0 or len(exam) == 0:
        continue

    exercise_points = math.floor(get_points_sum(exercises[0]) * 10 / 40)   # 0 - only one unique key
    exam_points = get_points_sum(exam[0])  # 0 - only one unique key

    grade = get_grade(exercise_points + exam_points)

    print(f"{name} {grade}")
