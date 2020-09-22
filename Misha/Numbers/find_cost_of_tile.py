def find_cost_of_tile():
    f = open('find_cost_of_tile.txt', 'r')
    data = f.readlines()
    data[0] = data[0].split(' ')
    w_floor = float(data[0][0])
    l_floor = float(data[0][1])
    w_tile = float(data[0][2])
    l_tile = float(data[0][3])
    price = float(data[1])
    print('Floor: ' + str(w_floor) + 'x' + str(l_floor))
    print('Tile: ' + str(w_tile) + 'x' + str(l_tile))
    print('Price: ' + str(price))
    quantity = (w_floor * l_floor) / (w_tile * l_tile)
    if quantity > round(quantity):
        quantity = round(quantity) + 1
    else:
        quantity = round(quantity)
    print("Total price: " + str(quantity * price))


if __name__=="__main__":
    print('This programm calculates the total cost of tile it would take to cover a floor\n')
    find_cost_of_tile()

