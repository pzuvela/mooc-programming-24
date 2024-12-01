# Write your solution here

import math

_n_students: int = int(input("How many students on the course? "))
_group_size: int = int(input("Desired group size?? "))

print(f"Number of groups formed: {math.ceil(_n_students / _group_size)}")