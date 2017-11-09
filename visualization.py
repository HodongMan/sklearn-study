from matplotlib import pyplot as plt
from collections import Counter


def normalCharts():
    
    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
    plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
    plt.title("Nominal GDP")
    plt.ylabel("Bllios of $won")
    plt.show()

def barCharts():

    movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
    num_oscars = [5, 11, 3, 8, 10]

    xs = [i + 0.1 for i, _ in enumerate(movies)]

    plt.bar(xs, num_oscars)
    plt.ylabel("# of Academy Awards")
    plt.title("My Favorite Movies")

    plt.xticks([i + 0.1 for i, _ in enumerate(movies)], movies)
    plt.show()

def histogram():

    grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
    decile = lambda grade : grade // 10 * 10
    histogram = Counter(decile(grade) for grade in grades)

    plt.bar([x for x in histogram.keys()], histogram.values(), 8)
    plt.axis([-5, 105, 0, 5])

    plt.xticks([10 * i for i in range(11)])
    plt.xlabel("Decile")
    plt.ylabel("# of Students")
    plt.title("Distribution of Exam 1 Grades")
    plt.show()

def lineCharts():

    variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
    total_error = [x + y for x, y in zip(variance, bias_squared)]
    xs = [i for i, _ in enumerate(variance)]
    plt.plot(xs, variance, 'g-', label='variance')
    plt.plot(xs, bias_squared, 'r-', label='bias^2')
    plt.plot(xs, total_error, 'b:', label='total error')

    plt.legend(loc=9)
    plt.xlabel("model compexity")
    plt.title("The Bias-Variance Tradeoff")
    plt.show()

def scatterCharts():

    friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
    minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    plt.scatter(friends, minutes)

    for label, friends_count, minute_count in zip(labels, friends, minutes):
        plt.annotate(label, xy=(friends_count, minute_count), xytext=(5, -5), textcoords='offset points')
    
    plt.show()

if __name__ == "__main__":

    scatterCharts()
