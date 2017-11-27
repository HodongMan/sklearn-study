from collections import Counter
import math
from random import choice, seed, random
from matplotlib import pyplot as plt


def randomKids():

    return choice(["boy", "girl"])

def uniformPDF(x):

    return 1 if x >= 0 and x < 1 else 0

def uniformCDF(x):

    if x < 0:
        return 0
    elif x < 1:
        return x
    else:
        return 1

def normalPDF(x, mu=0, sigma=1):
    
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu) ** 2 / 2 / sigma **2) / (sqrt_two_pi * sigma))

def normalCDF(x, mu=0, sigma=1):

    return(1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

def plotNormalPDF():

    xs = [x / 10.0 for x in range(-50, 50)]
    plt.plot(xs, [normalPDF(x, sigma=1) for x in xs], '-', label='mu=0, sigma=1')
    plt.plot(xs, [normalPDF(x, sigma=2) for x in xs], '--', label='mu=0, sigma=2')
    plt.plot(xs, [normalPDF(x, sigma=0.5) for x in xs], ':', label='mu=0, sigma=0.5')
    plt.plot(xs, [normalPDF(x, mu=-1) for x in xs], '-.', label='mu=-1, sigma=1')
    plt.legend()
    plt.title("Various Normal pdfs")
    plt.show()

def plotNormalCDF():

    xs = [x / 10.0 for x in range(-50, 50)]
    plt.plot(xs, [normalCDF(x, sigma=1) for x in xs], '-', label='mu=0, sigma=1')
    plt.plot(xs, [normalCDF(x, sigma=2) for x in xs], '--', label='mu=0, sigma=2')
    plt.plot(xs, [normalCDF(x, sigma=0.5) for x in xs], ':', label='mu=0, sigma=0.5')
    plt.plot(xs, [normalCDF(x, mu=-1) for x in xs], '-.', label='mu=-1, sigma=1')
    plt.legend(loc=4)
    plt.title("Various Normal cdfs")
    plt.show()

def inverseNormalCDF(p, mu=0, sigma=1, tolerance=0.00001):

    if mu != 0 or sigma != 1:
        return mu + sigma * inverseNormalCDF(p, tolerance=tolerance)

    low_z, low_p = -10.0, 0
    hi_z, hi_p = 10.0, 1
    
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2
        mid_p = normalCDF(mid_z)

        if mid_p < p:
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            hi_z, hi_p = mid_z, mid_p
        else:
            break

    return mid_z


def bernoulliTrial(p):

    return 1 if random() < p else 0

def binomail(n, p):

    return sum(bernoulliTrial(p) for _ in range(n))


def makeHist(p, n, num_points):

    data = [binomail(n, p) for _ in range(num_points)]

    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()],
            [v / num_points for v in histogram.values()],
            0.8,
            color='0.75')

    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))

    xs = range(min(data), max(data) + 1)
    ys = [normalCDF(i + 0.5, mu, sigma) - normalCDF(i - 0.5, mu, sigma) for i in xs]
    plt.plot(xs, ys)
    plt.title("Binomial Distribution vs. Normal Approximation")
    plt.show()

if __name__ == "__main__":


    """  
    both_girls = 0 # 두 아이가 모두 딸인 경우
    older_girl = 0 # 첫째가 딸인 경우
    either_girl = 0 # 둘 중 하나가 딸인 경우


    for _ in range(10000):

        younger = randomKids()
        older = randomKids()
        if older == "girl":
            older_girl += 1
        if older == "girl" and younger == "girl":
            both_girls += 1
        if older == "girld" or younger == "girl":
            either_girl += 1


    print("P(both | older) : ", both_girls / older_girl)
    print("P(both | either) : ", both_girls / either_girl)
    """
    #plotNormalPDF()
    #plotNormalCDF()
    makeHist(0.75, 100, 10000)
    
