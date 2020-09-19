def get_prime_factors(number,factors,start_index):
    for index in range(start_index,number):
        if number % index == 0:
            factors.append(index)
            number = number // index
            if number>=index:
                number=get_prime_factors(number,factors,index)
    return number


def main():
    print('This program finds all prime factors of entered Digit (if there are any)\n')
    number = int(input('Enter the number: '))
    factors=[]
    get_prime_factors(number, factors, 2)
    if factors==[] and number!=0 and number!=1:
        factors.append(number)
    if number>0:
        factors.append(1)
    print('Factors:',end=' ')
    for i in range(len(factors)):
        print(factors[i],end=' ')


if __name__=="__main__":
    main()