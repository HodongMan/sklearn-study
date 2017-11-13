import numpy as np
import math
from matplotlib import pyplot as plt


def makeMatrixShape(rows, cols):

    return np.arange(rows*cols).reshape(rows, cols)

def matrixCompute():

    a = np.array([20, 30, 40, 50])
    b = np.arange(4)

    print("{} - {} = {}".format(a, b, a-b))
    print("{} ** 2 = {}".format(b, b**2))

    A = np.array([[1, 1], [0, 1]])
    B = np.array([[2, 0], [3, 4]])

    print("{} * {} = {}".format(A, B, A.dot(B)))

def dot(v, w):

    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def scalar_multiply(c, v):

    return [c * v_i for v_i in v]

def sum_of_squares(v):

    return dot(v, v)


def makeGraphDotProductAsVectorProjection():

    v = [2, 1]
    w = [math.sqrt(.25), math.sqrt(.75)]
    c = dot(v, w)
    vonw = scalar_multiply(c, w)
    o = [0,0]

    plt.arrow(0, 0, v[0], v[1],
              width=0.002, head_width=.1, length_includes_head=True)
    plt.annotate("v", v, xytext=[v[0] + 0.1, v[1]])
    plt.arrow(0 ,0, w[0], w[1],
              width=0.002, head_width=.1, length_includes_head=True)
    plt.annotate("w", w, xytext=[w[0] - 0.1, w[1]])
    plt.arrow(0, 0, vonw[0], vonw[1], length_includes_head=True)
    plt.annotate(u"(v•w)w", vonw, xytext=[vonw[0] - 0.1, vonw[1] + 0.1])
    plt.arrow(v[0], v[1], vonw[0] - v[0], vonw[1] - v[1],
              linestyle='dotted', length_includes_head=True)
    plt.scatter(*zip(v,w,o),marker='.')
    plt.axis('equal')
    plt.show()

if __name__ == "__main__":

    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(matrix)
    print(matrix.shape)
    print(makeMatrixShape(100, 100))
    matrixCompute();
    makeGraphDotProductAsVectorProjection()
