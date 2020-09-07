import time
import math


def make_e(n):
    sum1 = 1
    for i in range(1, n + 1):
        sum1 = sum1 + (1 / math.factorial(i))
    result = round(sum1, n)
    return result


def main():
    n = int(input("Enter the n`th number to show the Euler's number digits after comma : "))
    start_time = time.time()
    print(make_e(n))
    end_time = time.time()
    total_time = end_time - start_time
    print('Time:', total_time)

if __name__ == "__main__":
    main()
