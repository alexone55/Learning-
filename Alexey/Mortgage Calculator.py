answer = input("Choose type of calc y/m/w/d/: ")
P = int(input("Principal Amount (initial loan balance): "))
i = float(input("Interest Rate: ")) / 100
t = int(input("Count of Years: "))
n = t * 12


def main():
    M = P * (i / 12 * (1 + i / 12) ** n) / ((1 + i / 12) ** n - 1)
    if answer.lower() == "m":
        MonthCalculation(M)
    elif answer.lower() == "y":
        YearCalculation(M)
    elif answer.lower() == "d":
        DailyCalculation(M)
    elif answer.lower() == "w":
        WeekCalculation(M)


def MonthCalculation(M):
    print("Your monthly " + str(round(M, ndigits=2)))


def DailyCalculation(M):
    daily = M / 30
    print("Your daily " + str(round(daily, ndigits=2)))


def WeekCalculation(M):
    week = M / 30 * 7
    print("Your weekly " + str(round(week, ndigits=2)))


def YearCalculation(M):
    year = M * 12
    print("Your yearly " + str(round(year, ndigits=2)))

if __name__ == "__main__":
     main()



