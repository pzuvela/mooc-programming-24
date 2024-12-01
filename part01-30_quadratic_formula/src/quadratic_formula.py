# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5

_a: float = float(input("Value of a: "))
_b: float = float(input("Value of b: "))
_c: float = float(input("Value of c: "))

_inner = sqrt(_b ** 2 - 4*_a*_c)
_denominator = 2 * _a

_positive_root = (-_b + _inner) / _denominator
_negative_root = (-_b - _inner) / _denominator

print(f"The roots are {_positive_root} and {_negative_root}")
