import time


def timer(function, n):
    start_time = time.time()
    result = function(n)
    end_time = time.time()
    total_time = end_time - start_time
    return result, total_time


def factorial_by_for(n):
    factorials = [1]
    for i in range(1, n + 1):
        factorials.append(factorials[i - 1] * i)
    return factorials[-1]


def factorial_by_while(n):
    factorials = [1]
    i = 1
    while i < (n + 1):
        factorials.append(factorials[i - 1] * i)
        i += 1
    return factorials[-1]


def factorial_by_recursion(n):
    if n != 1:
        return n * factorial_by_recursion(n - 1)
    else:
        return n


def main():
    n = int(input("Enter the number you want to find factorial : "))
    print('Recursion:', timer(factorial_by_recursion, n), "-time")
    print('while:    ', timer(factorial_by_while, n), "-time")
    print('for:      ', timer(factorial_by_for, n), "-time")


if __name__ == "__main__":
    main()
