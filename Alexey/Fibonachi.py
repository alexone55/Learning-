digit = int(input("Please type count of digits: "))
a, b = 0, 1

while len(str(b)) != digit + 1:
    print(b)
    a, b = b, a + b