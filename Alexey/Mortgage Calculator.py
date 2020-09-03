def main():
    answer = input("Choose type of calc y/m/w/d/: ")
    p = int(input("Principal Amount (initial loan balance): "))
    i = float(input("Interest Rate: ")) / 100
    t = int(input("Count of Years: "))
    n = t * 12
    m = p * (i / 12 * (1 + i / 12) ** n) / ((1 + i / 12) ** n - 1)

    if answer.lower() == "m":
        month_calculation(m)
    elif answer.lower() == "y":
        year_calculation(m)
    elif answer.lower() == "d":
        daily_calculation(m)
    elif answer.lower() == "w":
        week_calculation(m)


def month_calculation(m):
    print("Your monthly " + str(round(m, ndigits=2)))


def daily_calculation(m):
    daily = m / 30
    print("Your daily " + str(round(daily, ndigits=2)))


def week_calculation(m):
    week = m / 30 * 7
    print("Your weekly " + str(round(week, ndigits=2)))


def year_calculation(m):
    year = m * 12
    print("Your yearly " + str(round(year, ndigits=2)))


if __name__ == "__main__":
    main()



