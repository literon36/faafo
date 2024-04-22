from vector import *
import unittest

v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = v1 * 5
print(v2) # [[0.0], [5.0], [10.0], [15.0]]

v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
v2 = v1 * 5
print(v2) # [[0.0, 5.0, 10.0, 15.0]]
v2 = v1 / 2.0
print(v2) # [[0.0, 0.5, 1.0, 1.5]]

# v1 / 0.0 # ZeroDivisionError
# 2.0 / v1 # NotImplementedError

print(Vector([[0.0], [1.0], [2.0], [3.0]]).shape) # (4, 1)
print(Vector([[0.0], [1.0], [2.0], [3.0]]).values) # [[0.0], [1.0], [2.0], [3.0]]
print(Vector([[0.0, 1.0, 2.0, 3.0]]).shape) # (1, 4)
print(Vector([[0.0, 1.0, 2.0, 3.0]]).values) # [[0.0, 1.0, 2.0, 3.0]]

v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
print(v1.shape) # (4, 1)
print(v1.T()) # [[0.0], [1.0], [2.0], [3.0]]
print(v1.T().shape) # (1, 4)

v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
print(v2.shape) # (1, 4)
print(v2.T()) # [[0.0, 1.0, 2.0, 3.0]]
print(v2.T().shape) # (4, 1)

v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
print(v1.dot(v2)) # 18.0

v3 = Vector([[1.0, 3.0]])
v4 = Vector([[2.0, 4.0]])
print(v3.dot(v4)) # 14.0

print(v1.__repr__())
print(v1.__str__())