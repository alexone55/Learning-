def find_factorial():
    num=int(input('Enter the number: '))
    if num==0:
        print('Factorial: 0')
    else:
        for i in range(1,num):
            num*=i
        print('Factorial: '+str(num))


if __name__=="__main__":
    print('This program finds Factorial of the given number\n')
    find_factorial()