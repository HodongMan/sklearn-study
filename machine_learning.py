from collections import Counter
import math, random

def split_data(data, prop):

    """
        데이터를 [prob, 1 - prob] 비율로 나눔
    """
    results = [], []
    for row in data:
        results[0 if random.random() < prob else 1].append(row)
    return results

def train_test_split(x, y, test_pct):

    """
        훈련 데이터와 테스트 데이터를 나눔
    """
    data = zip(x, y)
    train, test = split_data(data, 1 - test_pct)
    x_train, y_train = zip(*train)
    x_test, y_test = zip(*test)
    return x_train, x_test, y_train, y_test

def accuracy(tp, fp, tn, fn):

    """
        데이터의 정확도를 계산하는 방법
    """
    correct = tp + tn
    total = tp + fp + fn + tn
    return correct / total

def precision(tp, fp, fn, tn):

    """
        정밀도는 양성으로 예측된 결과의 정확도를 계산
    """
    return tp / (tp + fp)

def recall(tp, fp, fn, tn):

    """
        재현율은 실제 양성 중 모델이 정확하게 양성으로 예측한 비율
    """
    return tp / (tp + fn)

def f1_score(tp, fp, fn, tn):

    """
        정밀도와 재현율을 결합해서 새로운 점수를 정의
    """
    p = precision(tp, fp, fn, tn)
    r = recall(tp, fp, fn, tn)

    return 2 * p * r / (p + r)


def


if __name__ == "__main__":
	
    print("accuracy(70, 4930, 13930, 981070)", accuracy(70, 4930, 13930, 981070))
    print("precision(70, 4930, 13930, 981070)", precision(70, 4930, 13930, 981070))
    print("recall(70, 4930, 13930, 981070)", recall(70, 4930, 13930, 981070))
    print("f1_score(70, 4930, 13930, 981070)", f1_score(70, 4930, 13930, 981070))
