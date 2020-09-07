import time
import decimal  # Lib for using decimal fractions
from decimal import *


def make_pi(n):
    decimal.getcontext().prec = n + 1
    C = 426880 * decimal.Decimal(10005).sqrt()
    K = 6.
    M = 1.
    X = 1
    L = 13591409
    S = L
    for i in range(1, n):
        M = M * (K ** 3 - 16 * K) / ((i + 1) ** 3)
        L += 545140134
        X *= -262537412640768000
        S += decimal.Decimal(M * L) / X
    pi = C / S
    return pi


def main():
    n = int(input("Enter the n`th number to show the Pi digits after comma : "))
    start_time = time.time()
    print(make_pi(n))
    end_time = time.time()
    total_time = end_time - start_time
    print('Time:', total_time)


if __name__ == "__main__":
    main()
