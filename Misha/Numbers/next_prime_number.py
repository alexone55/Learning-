def find_next_prime():
    prime = 1
    print('First prime number is ' + str(prime))
    string = str(input('Do you want to continue? Enter [y(yes)/n(no)]... '))
    while string == 'y':
        prime += 1
        factors = [prime]  # list of prime factors
        for i in range(1, prime // 2 + 1):
            if prime % i == 0:
                factors.append(i)
        if len(factors) == 2:
            print('Next prime number is ' + str(prime))
            string = str(input('Do you want to continue? Enter [y(yes)/n(no)]... '))


if __name__=="__main__":
    print('This program finds prime numbers until the user chooses to stop asking for the next one\n')
    find_next_prime()