def return_change(cost, summ):
    change = round(summ-cost,2)
    print('Change: ' + str(change))
    money_array = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.02, 0.01]
    for index in range(len(money_array)):
        counter = 0
        if change >= money_array[index]:
            while change >= money_array[index]:
                change = round(change-money_array[index],2)
                counter += 1
        if counter>0:
            print(str(money_array[index]) + 'x' + str(counter) + ' ', end='')
    return 0


if __name__ == "__main__":
    print('This program will figure out the change and money needed for the change\n')
    cost = float(input('Enter cost: '))
    summ = float(input('Enter sum of money: '))
    return_change(cost, summ)
