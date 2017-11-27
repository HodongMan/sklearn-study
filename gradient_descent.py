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

def safe(f):
    """define a new function that wraps f and return it"""
    def safe_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            return float('inf')         # this means "infinity" in Python
    return safe_f


#
#
# minimize / maximize batch
#
#

def minimize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    """use gradient descent to find theta that minimizes target function"""

    step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]

    theta = theta_0                           # set theta to initial value
    target_fn = safe(target_fn)               # safe version of target_fn
    value = target_fn(theta)                  # value we're minimizing

    while True:
        gradient = gradient_fn(theta)
        next_thetas = [step(theta, gradient, -step_size)
                       for step_size in step_sizes]

        # choose the one that minimizes the error function
        next_theta = min(next_thetas, key=target_fn)
        next_value = target_fn(next_theta)

        # stop if we're "converging"
        if abs(value - next_value) < tolerance:
            return theta
        else:
            theta, value = next_theta, next_value

def negate(f):
    """return a function that for any input x returns -f(x)"""
    return lambda *args, **kwargs: -f(*args, **kwargs)

def negate_all(f):
    """the same when f returns a list of numbers"""
    return lambda *args, **kwargs: [-y for y in f(*args, **kwargs)]

def maximize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    return minimize_batch(negate(target_fn),
                          negate_all(gradient_fn),
                          theta_0,
                          tolerance)


if __name__ == "__main__":

    plotEstimateDerivative()

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
