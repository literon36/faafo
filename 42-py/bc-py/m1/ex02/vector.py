from __future__ import annotations
from typing import Union, List

class Vector:
    def __init__(self, values :Union[list[list[float]], int, slice]) -> None:
        if isinstance(values, list):
            self.values = values
            if len(values) == 0:
                raise ValueError("Vector must not be empty")

            self.shape = (len(values), len(values[0]))
            #error when shape is not (1,n) or (n,1)
            if self.shape not in [(1, len(values[0])), (len(values), 1)]:
                raise ValueError("Vector must be of shape (1,n) or (n,1)")
            
        if isinstance(values, int):
            self.values = [[values] for _ in range(values)]
            self.shape = (values, 1)

        if isinstance(values, slice):
            self.values = [[i] for i in range(values.start, values.stop, values.step)]
            self.shape = (len(self.values), 1)


    def __add__(self, other :Vector) -> Vector:
        if self.shape != other.shape:
            raise ValueError("Vectors must have the same shape")
        return Vector([[self.values[i][j] + other.values[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])])

    def __radd__(self, other :Vector) -> Vector:
        if self.shape != other.shape:
            raise ValueError("Vectors must have the same shape")
        return other + self

    def __sub__(self, other :Vector) -> Vector:
        if self.shape != other.shape:
            raise ValueError("Vectors must have the same shape")
        return Vector([[self.values[i][j] - other.values[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])])

    def __rsub__(self, other :Vector) -> Vector:
        if self.shape != other.shape:
            raise ValueError("Vectors must have the same shape")
        return other - self

    def __truediv__(self, other :float) -> Vector:
        if other == 0:
            raise ZeroDivisionError("division by zero")
        return Vector([[self.values[i][j] / other for j in range(self.shape[1])] for i in range(self.shape[0])])

    def __rtruediv__(self, other :float) -> Vector:
        raise NotImplementedError("Division of scalar by vector is not defined here")

    def __mul__(self, other :float) -> Vector:
        return Vector([[other * self.values[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])])

    def __rmul__(self, other :float) -> Vector:
        return self * other

    def __str__(self) -> str:
        return f"Vector({self.values})"

    def __repr__(self) -> str:
        return str(self.values)



    def dot(self :Vector, v2 :Vector) -> float:
        if self.shape != v2.shape:
            raise ValueError("Vectors must have the same shape")
        return sum([self.values[i][j] * v2.values[i][j] for i in range(self.shape[0]) for j in range(self.shape[1])])

    def T(self) -> Vector:
        return Vector([[self.values[j][i] for j in range(self.shape[0])] for i in range(self.shape[1])])