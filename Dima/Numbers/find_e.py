from factorial_finder import factorial_by_recursion
from time_decorator import timer


def make_e(n):
    sum1 = 1
    for i in range(1, n + 1):
        sum1 = sum1 + (1 / factorial_by_recursion(i))
    result = round(sum1, n)
    return result


@timer
def main():
    n = int(input("Enter the n`th number to show the Euler's number digits after comma : "))
    print(make_e(n))


if __name__ == "__main__":
    main()
