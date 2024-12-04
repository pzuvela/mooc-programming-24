# Write your solution here

import math
from typing import (
    List,
    Tuple
)

mapping = (
    ((0, 14), 0),
    ((15, 17), 1),
    ((18, 20), 2),
    ((21, 23), 3),
    ((24, 27), 4),
    ((28, 30), 5)
)

def get_grade(n_points: int) -> int:
    for score_range, grade_value in mapping:
        if score_range[0] <= n_points <= score_range[1]:
            return grade_value
    raise ValueError(f"Illegal number of points : {n_points}!")


def process_line(line: str) -> Tuple[int, int]:
    n_exam_points, n_excercises = line.split(" ")
    n_exam_points: int = int(n_exam_points)
    n_excercises: int = int(n_excercises)
    n_excercise_points: int = math.floor(n_excercises / 10)
    failed_exam: bool = n_exam_points < 10
    n_points: int = n_exam_points + n_excercise_points
    return n_points, get_grade(n_points) if not failed_exam else 0


def print_statistics(points_grades: List[Tuple[bool, int]]):
    
    if len(points_grades) == 0:
        return
    
    points_: List[int] = []
    grades_: List[int] = []

    for p, g in points_grades:
        points_.append(p)
        grades_.append(g)

    print(f"Points average: {sum(points_) / len(points_):.1f}")
    print(f"Pass percentage: {sum(g > 0 for g in grades_) *100 / len(grades_):.1f}")
    print("Grade distribution:")

    for g in range(5, -1, -1):
        print(f"{g}: {'*' * sum(g_ == g for g_ in grades_)}")


points_grades_: List[Tuple[int, int]] = []

while True:

    line = input("Exam points and exercises completed: ")

    if line == "":
        print("Statistics:")
        print_statistics(points_grades_)
        break

    points_grades_.append(process_line(line))
