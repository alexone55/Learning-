def get_prime_factors():
    digit = int(input('Enter the digit: '))
    factors = []
    for i in range(1, digit // 2 + 1):  # twice less operations with "digit // 2 + 1"
        if digit % i == 0:
            factors.append(i)
    factors.append(digit)
    print('Factors: ', end='')
    for i in range(len(factors)):
        print(factors[i], end=' ')


if __name__=="__main__":
    print('This program finds all prime factors of entered Digit (if there are any)\n')
    get_prime_factors()