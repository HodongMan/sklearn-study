from collections import Counter
import math
from random import choice, seed

def randomKids():

    return choice(["boy", "girl"])

def uniformPDF(x):

    return 1 if x >= 0 and x < 1 else 0



if __name__ == "__main__":

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

    
