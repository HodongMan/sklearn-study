from probability import normalCDF, inverseNormalCDF
import math
import random


normalProbabilityBelow = normalCDF

def normalApproximationToBinomial(n, p):

    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma

def normalProbabilityAbove(lo, mu=0, sigma=1):

    return 1 - normalCDF(lo, mu, sigma)

def normalProbabilityBetween(lo, hi, mu=0, sigma=1):

    return normalCDF(hi, mu, sigma) - normalCDF(lo, mu, sigma)

def normalProbabilityOutSide(lo, hi, mu=0, sigma=1):

    return 1 - normalProbabilityBetween(lo, hi, mu, sigma)

def normalUpperBound(probability, mu=0, sigma=1):

    return inverseNormalCDF(probability, mu, sigma)

def normalLowerBound(probability, mu=0, sigma=1):

    return inverseNormalCDF(1 - probability, mu, sigma)

def normalTwoSidedBounds(probability, mu=0, sigma=1):

    tail_probability = (1 - probability) / 2

    upper_bound = normalLowerBound(tail_probability, mu, sigma)
    lower_bound = normalUpperBound(tail_probability, mu, sigma)

    return lower_bound, upper_bound

if __name__ == "__main__":

    mu_0, sigma_0 = normalApproximationToBinomial(1000, 0.5)

    print("mu 0", mu_0)
    print("sigma 0", sigma_0)
    print("normal two sided bound(0.95, mu_0, sigma_0)", normalTwoSidedBounds(0.95, mu_0, sigma_0))
    print()
    print("power of a test")

    print("95% bounds based on assumption p is 0.5")

    lo, hi = normalTwoSidedBounds(0.95, mu_0, sigma_0)

    print("actual mu and sigma based on p = 0.55")
    mu_1, sigma_1 = normalApproximationToBinomial(1000, 0.55)
    print("mu_1", mu_1)
    print("sigma_1", sigma_1)

    type_2_probability = normalProbabilityBetween(lo, hi, mu_1, sigma_1)
    power = 1 - type_2_probability

    print("type 2 probability", type_2_probability)
    print("power", power)
    print()

    print("one sided test")

    hi = normalUpperBound(0.95, mu_0, sigma_0)
    print("hi", hi)

    type_2_probability = normalProbabilityBelow(hi, mu_1, sigma_1)
    power = 1 - type_2_probability

    print("type 2 probability", type_2_probability)
    print("power", power)

