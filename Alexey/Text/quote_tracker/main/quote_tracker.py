def main():
    stock = input('Enter a symbol: ')
    quote_tracker(stock)


def quote_tracker(stock, previous=[]):
    previous.append(stock)
    while True:
        stock = input('Enter next symbol: ')
        if stock == '\q':
            break
        elif len(previous) > 0:
            return logic(ord(stock), ord(previous[-1]))
        previous.append(stock)


def logic(stock, previous):
    if stock < previous:
        result = previous - stock
        return '-' + str(result) + ' Down'
    elif stock > previous:
        result = stock - previous
        return '+' + str(result) + ' Up'
    elif stock == previous:
        return 'Equal'


if __name__ == '__main__':
    main()
