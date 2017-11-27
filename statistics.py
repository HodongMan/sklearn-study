from __future__ import division

from collections import Counter
from matplotlib import pyplot as plt
from matrix_numpy import sum_of_squares, dot
import math

class StatisticsOfFriends:

    def __init__(self):

        self.friends_list = [100,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

    def count(self):
        
        return len(self.friends_list)

    def largestValue(self):

        return max(self.friends_list)

    def smallestValue(self):
        
        return min(self.friends_list)

    def meanValue(self):

        return sum(self.friends_list) / len(self.friends_list)

    def medianValue(self):

        n = len(self.friends_list)
        sorted_f = sorted(self.friends_list)
        midpoint = n // 2

        if n % 2 == 1:
            return sorted_f[midpoint]
        else:
            low_value = midpoint - 1
            high_value = midpoint
            return (sorted_f[low_value] + sorted_f[high_value]) / 2

    def quantile(self, percent):

        p_index = int(percent * len(self.friends_list))
        return sorted(self.friends_list)[p_index]

    def modeValue(self):
        
        """
            데이터에서 가장 자주 나오는 값 구하기
        """
        counts = Counter(self.friends_list)
        max_count = max(counts.values())
        return [x_i for x_i, count in counts.items() if count == max_count]

    def dispersion(self):
        """
            산포도 값
        """
        return max(self.friends_list) - min(self.friends_list)

    def decreaseMeanValue(self):

        mean_value = self.meanValue()
        return [x_i - mean_value for x_i in self.friends_list]

    def variance(self):

        """
            분산
        """
        n = len(self.friends_list)
        deviations = self.decreaseMeanValue()
        return sum_of_squares(deviations) / (n - 1)

    def standardDeviation(self):

        """
            표준편차
        """

        return math.sqrt(self.variance())

    def interquantile(self):

        """
            상위 75%와 25%의 차이
        """

        return self.quantile(0.75) - self.quantile(0.25)

    def makeNumberOfFriendsHistogram(self):

        friend_counts = Counter(self.friends_list)
        xs = range(101)
        ys = [friend_counts[x] for x in xs]
        plt.bar(xs, ys)
        plt.axis([0,101,0,25])
        plt.title("Histogram of Friend Counts")
        plt.xlabel("# of friends")
        plt.ylabel("# of people")
        plt.show()

def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0 # if no variation, correlation is zero

def mean(x):
    return sum(x) / len(x)

def median(v):
    """finds the 'middle-most' value of v"""
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:
        # if odd, return the middle value
        return sorted_v[midpoint]
    else:
        # if even, return the average of the middle values
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2

def quantile(x, p):
    """returns the pth-percentile value in x"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]

def mode(x):
    """returns a list, might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
            if count == max_count]

# "range" already means something in Python, so we'll use a different name
def data_range(x):
    return max(x) - min(x)

def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)

def standard_deviation(x):
    return math.sqrt(variance(x))



if __name__ == "__main__":

    stats = StatisticsOfFriends()

    #stats.makeNumberOfFriendsHistogram()
    print("number of freinds : ", stats.count())
    print("largest of freinds : ", stats.largestValue())
    print("smallest of firends : ", stats.smallestValue())
    print("mean of friends : ", stats.meanValue())
    print("median of friends : ", stats.medianValue())
    print("quantile of friends :", stats.quantile(0.1))
    print("quantile of friends :", stats.quantile(0.25))
    print("quantile of friends :", stats.quantile(0.75))
    print("quantile of friends :", stats.quantile(0.90))
    print("modeValue of friends : ", stats.modeValue())
    print("dispersion of friends : ", stats.dispersion())
    print("variance of freinds : ", stats.variance())
    print("standard deviation of friends :", stats.standardDeviation())
    print("inter quantile of friends :", stats.interquantile())
