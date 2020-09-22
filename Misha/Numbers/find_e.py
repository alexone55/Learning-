def find_e():
    n = int(input('Enter the N: '))
    e = 0
    h = 1  # help variable to avoid creation function to find the factorial
    for i in range(1, 100):
        e += 1 / h
        h *= i
    # 2,7182818284
    print(round(e, n))


if __name__=="__main__":
    print('This program finds e to the Nth Digit\n')
    find_e()