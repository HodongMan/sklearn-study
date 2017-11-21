from functools import partial, reduce
import math

class Vector:

    "class 형태의 Vector 더하기와 빼기가 가능하다"

    def __init__(self, vector):

        self._vectors = vector

    def __add__(self, vector):

        return Vector([v_i + w_i for v_i, w_i in zip(self._vectors, vector)])

    def __mul__(self, vector):

        return Vector([v_i - w_i for v_i, w_i in zip(self._vectors, vector)])

    def __iter__(self):

        for vector in self._vectors:
            yield vector

    def sumAllVectors(self):

        return sum(self._vectors)

    def multiplyScalar(self, scalar):

        self._vectors = [scalar * v_i for v_i in self._vectors]


def addVector(v, w):
    """
        list 형태의 vector의 더하기를 구하는 function
    """
    return [v_i + w_i for v_i, w_i in zip(v, w)]

def subVector(v, w):

    """
        list 형태의 vetor의 빼기를 구하는 function
    """

    return [v_i - w_i for v_i, w_i in zip(v, w)]


def sumAllVectors(v, w):

    """
        list 형태의 vector의 각 성분들의 합
    """
    return reduce(vector_add, vectors)


def multiplyScalar(c, v):

    return [c * v_i for v_i in v]

def vector_mean(vectors):

    n = len(vectors)
    return multiplyScalar(1/n, sumAllVectors(vectors))

def distance(v, w):

    return magnitude(subVector(v, w))

def dot(v, w):

    """
        vector의 내적
    """

    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def squareVector(v):

    return dot(v, v)

def magnitude(v):
    return math.sqrt(squareVector(v))


if __name__ == "__main__":

    v1 = Vector([70, 170, 40])
    v2 = Vector([90, 180, 60])

    v1 = v1 + v2

    print(v1._vectors)
    print(v1.sumAllVectors())
