for i in [1, 2, 3, 4, 5]:
    print(i)
    for j in [1, 2, 3, 4, 5]:
        print(j)
        print(i + j)
print("done looping")


import re
my_regex = re.comple("[0-9]", re.I)

import matplotlib.pyplot as plt


from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()


def double(x):

    """
        이곳은 함수의 대한 설명을 적어 놓는 공간이다
        예를 들어 '이 함수는 입력된 변수에 2를 곱한 값을 출력해준다 '
        라는 설명을 축하라 수도 있다.
    """

    return x * 2

def apply_to_one(f):

    return f(1)

my_double = double
x = apply_to_one(my_double)

y = apply_to_one(lambda x : x + 4) # lambda는 후크함수로 많이 쓰인다

another_double = lambda x : 2 * x
def another_double(x):
    return 2 * x

def my_print(message='my default message'):
    print (message)

my_print("Hello")
my_print()

single_quoted_string = 'data science from 007'
double_quoted_string = "data science from 007"

try:
    print (0 / 0)
except ZeroDivisionError:
    print ("Cannot divide by zero")

raise ZeroDivisionError("Cannot divide by zero")

integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [integer_list, heterogeneous_list, []]

list_length = len(integer_list)
list_sum = sum(integer_list)

1 in [1, 2, 3]
0 in [1, 2, 3]

x = [1, 2, 3]
x.append(0)

x, y = [1, 2]

my_tuple = (1, 2)
my_tuple[1] = 3

def sum_add_product(x, y):
    return (x + y), (x * y)


empty_dict = {}
empty_dict2 = dict()
grades = {"Joel" : 80, "Tim" : 95}

joels_grade = grades["Joel"]

tweet = {
    "user" : "Hodong",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]

}

tweet_keys = tweet.keys()
tweet_values = tweet.values()
tweet_imtes = tweet.itmes()

if 1 > 2:
    message = "if only 1 were greater than two..."
elif 1 > 3:
    message = "elif stands for 'else if'"
else:
    message = "when all esle fails use else"

for x in range(10):
    print(x, "is less than 10")



