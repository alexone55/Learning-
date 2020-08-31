digit = int(input("Please type count of digits: "))
e = 0

for i in range(1, 100000000):
    e += ((1+(1/ i)) ** i)
    e = e / i

result = e
print(round(result, digit))