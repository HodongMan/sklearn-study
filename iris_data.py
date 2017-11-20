from IPython.display import display
import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt
import pandas as pd
import mglearn

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


class IrisDataClassifier:

    def __init__(self):
        self.initialize()

    def initialize(self):

        self.iris_dataset = load_iris()
        self.X_train, self.X_test, self.Y_train, self.Y_test = \
            train_test_split(self.iris_dataset['data'], self.iris_dataset['target'], random_state = 0)

    def printStatusIrisData(self):

        print("iris_dataset의 키 : \n{}".format(self.iris_dataset.keys()))
        print(self.iris_dataset['DESCR'][:193] + "\n.....")
        print("타깃의 이름 : {}".format(self.iris_dataset['target_names']))
        print("특성의 이름 : \n{}".format(self.iris_dataset['feature_names']))
        print("data의 타입 : {}".format(type(self.iris_dataset['data'])))
        print("data의 크기 : {}".format(self.iris_dataset['data'].shape))
        print("data의 처음 다섯 행 : \n{}".format(self.iris_dataset['data'][:5]))
        print("target의 타입 : {}".format(type(self.iris_dataset['target'])))
        print("target의 크기 : {}".format(self.iris_dataset['target'].shape))
        print("타깃 : \n{}".format(self.iris_dataset['target']))

    def printScaleOfIrisData(self):
        
        print("X_train 크기 : {}".format(self.X_train.shape))
        print("Y_train 크기 : {}".format(self.Y_train.shape))
        print("X_test 크기 : {}".format(self.X_test.shape))
        print("Y_test 크기 : {}".format(self.Y_test.shape))


    def pltShowIrisData(self):

        iris_dataframe = pd.DataFrame(self.X_train, columns=self.iris_dataset.feature_names)
        pd.plotting.scatter_matrix(iris_dataframe, c=self.Y_train, figsize=(15, 15), marker='o', hist_kwds={'bins' : 20}, s=60, alpha=.8, cmap=mglearn.cm3)
        plt.show()

    def CassifierToIrisDataAndPrint(self, x_data):

        knn = KNeighborsClassifier(n_neighbors=1)
        knn.fit(self.X_train, self.Y_train)
        print("X_new.shape : {}".format(x_data.shape))

        print(knn);


        prediction = knn.predict([x_data])
        print("예측 : {}".format(prediction))
        print("예측한 타깃의 이름 : {}".format(self.iris_dataset['target_names'][prediction]))

        y_pred = knn.predict(x_data)
        print("테스트 세트에 대한 예측값 : \n{}".format(y_pred))
        print("테스트 세트의 정확도 : {:.2f}".format(np.mean(y_pred == self.Y_test)))
        print("테스트 세트의 정확도 : {:.2f}".format(knn.score(self.X_test, self.Y_test)))



if __name__ == "__main__":

    
    iris = IrisDataClassifier()

    #iris.printStatusIrisData()
    #iris.printScaleOfIrisData()
    #iris.pltShowIrisData()
    
    iris.CassifierToIrisDataAndPrint(np.array([5, 2.9, 1.0, 0.2]))

    
