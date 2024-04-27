from re import S
from vector import *
import unittest

class TestVector(unittest.TestCase):
    def test_multiplication(self):
        v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
        v2 = v1 * 5
        print(v2)
        self.assertEqual(v2.values, [[0.0], [5.0], [10.0], [15.0]])

        v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
        v2 = v1 * 5
        print(v2)
        self.assertEqual(v2.values, [[0.0, 5.0, 10.0, 15.0]])
        v2 = v1 / 2.0
        print(v2)
        self.assertEqual(v2.values, [[0.0, 0.5, 1.0, 1.5]])

    def test_error(self):
        v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
        with self.assertRaises(ZeroDivisionError):
            v2 = v1 / 0.0
        with self.assertRaises(NotImplementedError):
            v2 = 2.0 / v1

    def test_shape_values(self):
        v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
        v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
        print(v1.shape)
        print(v1.values)
        print(v2.shape)
        print(v2.values)
        self.assertEqual(v1.shape, (4, 1))
        self.assertEqual(v1.values, [[0.0], [1.0], [2.0], [3.0]])
        self.assertEqual(v2.shape, (1, 4))
        self.assertEqual(v2.values, [[0.0, 1.0, 2.0, 3.0]])

    def test_transpose(self):
        v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
        print(f"{v1.shape=}")
        print(f"{v1.T()=}")
        print(f"{v1.T().shape=}")
        print(f"{v1.T().T()=}")
        print(f"{v1.T().T().shape=}")
        self.assertEqual(v1.shape, (4, 1))
        self.assertEqual(v1.T(), [[0.0, 1.0, 2.0, 3.0]])
        self.assertEqual(v1.T().shape, (1, 4))

        v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
        print(v2.shape)
        print(v2.T())
        print(v2.T().shape)
        self.assertEqual(v2.shape, (1, 4))
        self.assertEqual(v2.T(), [[0.0], [1.0], [2.0], [3.0]])
        self.assertEqual(v2.T().shape, (4, 1))

    def test_dot(self):
        v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
        v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
        print(v1.dot(v2))
        self.assertEqual(v1.dot(v2), 18.0)

        v3 = Vector([[1.0, 3.0]])
        v4 = Vector([[2.0, 4.0]])
        print(v3.dot(v4))
        self.assertEqual(v3.dot(v4), 14.0)

    def test_str_repr(self):
        v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
        print(v1.__str__())
        print(v1.__repr__())
        self.assertEqual(v1.__str__(), "Vector([[0.0], [1.0], [2.0], [3.0]])")
        self.assertEqual(v1.__repr__(), "[[0.0], [1.0], [2.0], [3.0]]")

if __name__ == "__main__":
    unittest.main()