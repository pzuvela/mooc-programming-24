# write your solution here
import os
from typing import Type


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


def get_exercise_sum(exercise_datum) -> int:
    return sum(exercise_datum[col] for col in list(exercise_datum.keys())[1:])


def get_data_by_id(data: list[dict[str, str | int]], datum_id: int) -> list[dict[str, str | int]]:
    return [datum for datum in data if datum["id"] == datum_id]


def get_path(filename: str) -> str:
    path_: str = os.path.join(os.path.dirname(__file__), filename)
    return path_


student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

# student_info_ = read_csv(get_path(student_info), str)
# exercise_data_ = read_csv(get_path(exercise_data), int)

student_info_ = read_csv(student_info, str)
exercise_data_ = read_csv(exercise_data, int)

for student in student_info_:

    name = f"{student['first']} {student['last']}"

    exercises = get_data_by_id(exercise_data_, student['id'])

    if len(exercises) == 0:
        continue

    print(f"{name} {get_exercise_sum(exercises[0])}")  # 0 - only one unique key
