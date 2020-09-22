def pow(value, power):
    result=1
    if power != 0:
        for index in range(power):
            result *= value
    return result


if __name__=="__main__":
    print('This program requires two integers and returns value in power\n')
    value=int(input('Enter value: '))
    power=int(input('Enter power: '))
    print('Result: '+str(pow(value,power)))
