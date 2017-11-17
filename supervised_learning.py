from IPython.display import display
import numpy as np
from scipy import sparse
from matplotlib import pyplot as plt
import pandas as pd
import mglearn

from sklearn.datasets import load_breast_cancer, load_boston

class SupervisedLearning:

    def __init__(self):
        
        self.loadForgeData()

    def loadForgeData(self):
        
        self.X, self.Y = mglearn.datasets.make_forge()
 

    def makeScatter(self):
        
        mglearn.discrete_scatter(self.X[:,0], self.X[:,1], self.Y)
        plt.legend(["class 0", "class 1"], loc=4)
        plt.xlabel("first characteristic")
        plt.ylabel("second characteristic")
        plt.show()
        print("X.shape : {}".format(self.X))

    def makeWave(self):

        X, Y = mglearn.datasets.make_wave(n_samples=40)
        plt.plot(X, Y, 'o')
        plt.ylim(-3, 3)
        plt.xlabel("characteristic")
        plt.ylabel("target")
        plt.show()

    def loadCancerData(self):

        self.cancer = load_breast_cancer()
        print("Cancer.keys() : \n{}".format(self.cancer.keys()))

    def printCancerDataform(self):

        print("유방암 데이터의 형태 : {}".format(self.cancer.data.shape))
        print("클래스별 샘플 개수 : \n{}".format(
            {n : v for n, v in zip(self.cancer.target_names, np.bincount(self.cancer.target))}))
        #양성 : benign 악성 : malignant
        print("특성 이름 : \n{}".format(self.cancer.feature_names))

    def loadBostonData(self):

        self.boston = load_boston()
        print("데이터의 형태 : {}".format(self.boston.data.shape))

    def loadExtendsBoston(self):

        self.X, self.Y = mglearn.datasets.load_extended_boston()
        print("X.shape : {}".format(self.X.shape))

if __name__ == "__main__":

    sl = SupervisedLearning()
    sl.loadBostonData()
    sl.loadExtendsBoston()
