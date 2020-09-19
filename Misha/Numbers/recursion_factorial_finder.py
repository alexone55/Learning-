def factorial_finder(start_value, start_index, number):
    start_value*=(start_index+1)
    start_index+=1
    if start_index<number:
        start_value = factorial_finder(start_value, start_index, number)
    return start_value


def main():
    print('This program finds factorial of Nth number using recursion')
    number=int(input('Enter the Nth number: '))
    factorial = factorial_finder(1, 0, number)
    print('Factorial of '+str(number)+': '+str(factorial))


if __name__=="__main__":
    main()