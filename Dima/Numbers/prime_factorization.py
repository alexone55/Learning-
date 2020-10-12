def prime_factorization(num):
    answer = []
    digit = 2
    while digit * digit <= num:
        if num % digit == 0:
            answer.append(digit)
            num //= digit
        else:
            digit += 1
    if num > 1:
        answer.append(num)
    return answer


def main():
    num = int(input('Enter your number: '))
    print(*prime_factorization(num))


if __name__ == "__main__":
    main()
