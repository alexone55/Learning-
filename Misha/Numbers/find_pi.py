def find_pi():
    n = int(input('Enter the N: '))
    pi = 0
    for i in range(1, 1000000):  # with this alhorythm 1e6 iterations to have accuracy for 5 values
        pi += 1 / (i ** 2)
    # 3,1415926535
    pi = (pi * 6) ** 0.5
    print(round(pi, n))


if __name__ == "__main__":
    print('This program finds PI to the Nth Digit\n')
    find_pi()
