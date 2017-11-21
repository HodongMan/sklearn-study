from collections import Counter
import math, random
from matplotlib import pyplot as plt
from linear_algebra import distance, subVector, multiplyScalar
from functools import reduce


def sumOfSquare(v):

    return sum(v_i ** 2 for v_i in v)

def differenceQuotient(f, x, h):

    return (f(x + h) - f(x)) / h

def plotEstimateDerivative():

    """
        실제 도함수와
        도함수 추론의 결과가 일치하는지
        확인하는 function
    """

    square = lambda x : x * x
    derivative = lambda x : 2 * x

    derivativeEstimate = lambda x : differenceQuotient(square, x, h=0.00001)

    x = range(-10, 10)
    plt.title("Actual Derivatives vs Estimates")
    plt.plot(x, list(map(derivative, x)), 'rx', label="Actual")
    plt.plot(x, list(map(derivativeEstimate, x)), 'b+', label="Estimate")
    plt.legend(loc=9)
    plt.show()


def partialDifferenceQuotient(f, v, i, h):

    """
        함수 f의 i번째 편도함수가 v에서 가지는 값
    """
    w = [v_j + (h if j == i else 0) for j, v_j in enumerate(v)]

    return (f(w) - f(v)) / h

def estimateGradient(f, v, h = 0.00001):

    """
        일반적인 도함수와 같은 방법으로 gradient의 근사값을 구할 수 있는 방법
    """

    return [partialDifferenceQuotient(f, v, i, h) for i, _ in enumerate(v)]

def step(v, direction, step_size):

    return [v_i + step_size * direction_i for v_i, direction_i in zip(v, direction)]

def sumOfSquaresGradient(x):

    return [2 * v_i for v_i in v]


if __name__ == "__main__":

    #plotEstimateDerivative()

    """
    미분법으로 최소한의 값 찾으려고 노력하기
    v = [random.randint(-10, 10) for i in range(3)]
    tolerance = 0.0000001

    while True:
        gradient = sumOfSquaresGradient(v)
        next_v = step(v, gradient, -0.01)
        if distance(next_v, v) < tolerance:
            break
        v = next_v

    print(v)
    """
