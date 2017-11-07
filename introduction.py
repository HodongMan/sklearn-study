from collections import Counter, defaultdict
from matplotlib import pyplot as plt


class UsersFriendsContainer:

    def __init__(self, user_list, friends_list):

        self.users = user_list
        self.friendships = friends_list
        self.friendsListInitialize()

    def __getitem__(self, index):

        return self.users[index]

    def friendsListInitialize(self):
        
        for user in self.users:
            user["friends"] = []

        for i, j in friendships:

            users[i]["friends"].append(users[j])
            users[j]["friends"].append(users[i])

    def numberOfFriends(self, index):

        if isinstance(index, int):
            return len(self.users[i]["friends"])
        else:
            return len(index["friends"])

    def totalFriendsConnection(self):

        return sum(self.numberOfFriends(user) for user in self.users)

    def averageFriendsConnection(self):

        return self.totalFriendConnection() / len(self.users)

    def numberOfFriendsById(self):

        num_friends_by_id = [(user["id"], self.numberOfFriends(user)) for user in self.users]
        return sorted(num_friends_by_id, key=lambda user : user[1], reverse=True)

    def friendsOfFriendsIdsBad(self, index):

        if isinstance(index, int):
            return [foaf["id"]
                for friends in index["friends"]
                for foaf in firends["friends"]]

        else:
            return [foaf["id"]
                for friends in self.users[index]["friends"]
                for foaf in firends["friends"]]

    def isSameUser(self, user, other_user, key=True):

        if key:
            return user["id"] == other_user["id"]
        else:
            return user["id"] != other_user["id"]

    def isUserFriendship(self, user, other_user, key=True):

        return all(self.isSameUser(friend, other_user, key=key) for friend in user["friends"])

    def friendsOfFriends(self, index):

        if isinstance(index, int):
            return Counter(foaf["id"]
                for friend in self.users[index]["friends"]
                for foaf in friend["friends"]
                if self.isSameUser(self.users[index], foaf, key=False)
                and self.isUserFriendship(self.users[index], foaf, key=False))
        else:
            return Counter(foaf["id"]
                for friend in index["friends"]
                for foaf in friend["friends"]
                if self.isSameUser(index, foaf, key=False)
                and self.isUserFriendship(index, foaf, key=False))


users = [

    {"id" : 0, "name" : "Hero"},
    {"id" : 1, "name" : "Dunn"},
    {"id" : 2, "name" : "Ronaldo"},
    {"id" : 3, "name" : "Hodong"},
    {"id" : 4, "name" : "Messi"},
    {"id" : 5, "name" : "Iniesta"},
    {"id" : 6, "name" : "Clive"},
    {"id" : 7, "name" : "Lil wayne"},
    {"id" : 8, "name" : "Dr.dre"},
    {"id" : 9, "name" : "Nas"},
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), 
        (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


############################################################################

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

def data_scientists_who_like(target_interest):

    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]




if __name__ == "__main__":

    user_friends = UsersFriendsContainer(users, friendships)
    print(user_friends.numberOfFriendsById())
    print(user_friends.friendsOfFriends(users[3]))
