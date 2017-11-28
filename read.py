import csv
from collections import namedtuple

Item = namedtuple("Item", ("name", "normal_price", "price", "sales_quantity_9to10", "sales_quantity_10to11"))
rankedItem = namedtuple("rankedItem", ("rank",  'changed_rank', 'name', 'normal_price', 'price', 'discount_price'))

class BestItemList:


    def __init__(self, csvfile, encoding=''):

        self.csvfile = csvfile
        self.encoding = encoding
        self.item_list = list()
        self.initialize()

    def initialize(self):

        with open(self.csvfile, newline='', encoding=self.encoding) as csvfile:

            data = csv.reader(csvfile)
            self.item_list = [Item(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4]))
                    for row in data]

    def calculateSalesQuantity9to10(self):

        return sorted(self.item_list, key=lambda x : x.price * x.sales_quantity_9to10, reverse=True)

    def calculateSalesQuantity10to11(self):

        return sorted(self.item_list, key=lambda x : x.price * x.sales_quantity_10to11, reverse=True)

    def makeRankingList(self):

        result_item_list_9to10 = self.calculateSalesQuantity9to10()
        result_item_list_10to11 = self.calculateSalesQuantity10to11()
        

        for index, result in enumerate(result_item_list_10to11):

            ranking_9to10 = str(result_item_list_9to10.index(result) - index)
            discount_rate = int(((result.normal_price - result.price) / result.normal_price) * 100)
            if ranking_9to10 == "0":
                ranking_9to10 = '-'

            yield rankedItem(index + 1, ranking_9to10, result.name, '{:,}'.format(result.normal_price), '{:,}'.format(result.price), str(discount_rate) + '%')


    def printSalesRanking(self):


        for item in self.makeRankingList():

            print("현재 순위 : {} 순위 변동 : {} 상품명 : {} 정상가 : {} 판매가 : {} 할인율 : {}"
                    .format(item.rank, item.changed_rank, item.name, item.normal_price, item.price, item.discount_price))

if __name__ == "__main__":

    bestItemList = BestItemList("2017_be_sheet.csv", 'euc-kr')

    bestItemList.printSalesRanking()




