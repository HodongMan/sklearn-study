from collections import Counter, defaultdict
from functools import partial, reduce

from linear_algebra import shape, get_row, get_column, make_matrix, \
        vector_mean, vector_sum, dot, magnitude, vector_subtract, scalar_multiply
from statistics import correlation, standard_deviation, mean
from probability import inverseNormalCDF
from gradient_descent import maximize_batch

import math, random, csv
from matplotlib import pyplot as plt
import dateutil.parser


"""
    1차원 데이터 분석

"""


def bucketize(point, bucket_size):

    """
        연속된 데이터를 이산 데이터로 수정
    """
    return bucket_size * math.floor(point / bucket_size)

def makeHistogram(points, bucket_size):

    """
        histogram data 만들기
    """

    return Counter(bucketize(point, bucket_size) for point in points)

def plotHistogram(points, bucket_size, title=""):

    histogram = makeHistogram(points, bucket_size)


    plt.bar(list(histogram.keys()), histogram.values(),  width=bucket_size)
    plt.title(title)
    plt.plot()
    plt.show()



"""
    2차원 데이터 분석
"""

def randomNormal():

    return inverseNormalCDF(random.random())


def makeScatter():

    xs = [randomNormal() for _ in range(1000)]
    ys1 = [x + randomNormal() / 2 for x in xs]
    ys2 = [-x + randomNormal() / 2 for x in xs]

    plt.scatter(xs, ys1, marker='.', color='black', label='ys1')
    plt.scatter(xs, ys2, marker='.', color='gray', label='ys2')
    plt.xlabel('xs')
    plt.ylabel('ys')
    plt.legend(loc=9)
    plt.show()

"""
    다차원 데이터 분석
"""


def correlationMatrix(data):

    _, num_columns = shape(data)

    def matrix_entry(i ,j):
        return correlation(get_column(data, i), get_column(data, j))

    return make_matrix(num_columns, num_columns, matrix_entry)

def makeScatterPlotByMatrix():

    num_points = 100

    def random_row():

        row = [None] * 4
        row[0] = randomNormal()
        row[1] = -5 * row[0] + randomNormal()
        row[2] = row[0] + row[1] + 5 * randomNormal()
        row[3] = 6 if row[2] > -2 else 0
        return row
    
    data = [random_row() for _ in range(num_points)]

    _, num_columns = shape(data)
    fig, ax = plt.subplots(num_columns, num_columns)

    for i in range(num_columns):
        for j in range(num_columns):

            if i != j:
                ax[i][j].scatter(get_column(data, j), get_column(data, i))
            else:
                ax[i][j].annotate("series " + str(i), (0.5, 0.5), xycoords='axes fraction', ha='center', va='center')

            if i < num_columns -1:
                ax[i][j].xaxis.set_visible(False)
            if j > 0:
                ax[i][j].yaxis.set_visible(False)


    ax[-1][-1].set_xlim(ax[0][-1].get_xlim())
    ax[0][0].set_ylim(ax[0][1].get_ylim())

    plt.show()


"""
    차원 축소

"""

def scale(data_matrix):

    num_rows, num_cols = shape(data_matrix)
    means = [mean(get_colum)]

def deMeanMatrix(A):

    nr, nc = shape(A)
    column_means, _ = scale(A)
    return makeMatrix(nr, nc, lambda i, j : A[i][j] - column_means[j])

if __name__ == "__main__":

    # -100과 100사이의 분포
    uniform = [random.randrange(-100, 101) for _ in range(10000)]

    # 평균이 0이고 표준편차가 57인 정규분포
    normal = [57 * inverseNormalCDF(random.random()) for _ in range(10000)]

    #plotHistogram(uniform, 10, "Uniform Histogram")
    #plotHistogram(normal, 10, "Normal Histogram")

    #makeScatter()
    makeScatterPlotByMatrix()
