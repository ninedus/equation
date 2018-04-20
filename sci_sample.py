from scipy import linalg as la
from scipy import optimize

import sympy
import numpy as np
import matplotlib.pyplot as plt

sympy.init_printing()

A = sympy.Matrix([[2, 3], [5, 4]])
b = sympy.Matrix([4, 3])
print(A.rank())
print(A.condition_number())
