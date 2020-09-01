def find_distance():
    print('Enter First city coordinates:')
    x1 = float(input('\tX: '))
    y1 = float(input('\tY: '))
    print('Enter Second city coordinates:')
    x2 = float(input('\tX: '))
    y2 = float(input('\tY: '))
    if x1 > x2:
        xlen = x1 - x2
    else:
        xlen = x2 - x1
    if y1 > y2:
        ylen = y1 - y2
    else:
        ylen = y2 - y1
    if ylen == 0 and xlen != 0:
        distance = xlen
    elif xlen == 0 and ylen != 0:
        distance = ylen
    elif xlen == 0 and ylen == 0:
        distance = 0
    else:
        distance = (xlen ** 2 + ylen ** 2) ** (1 / 2)
    print('Distance: ' + str(distance))


if __name__=="__main__":
    print('This program calculates distance between two cities\n'
          'This program may require finding coordinates for the cities like latitude and longitude.')
    find_distance()