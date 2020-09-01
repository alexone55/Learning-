def main():
    digit = int(input("Please type count of digits: "))
    fibonachi(digit)



def fibonachi(digit):
    a, b = 0, 1
    while len(str(b)) != digit + 1:
        print(b)
        a, b = b, a + b

if __name__ == '__main__':
    main()