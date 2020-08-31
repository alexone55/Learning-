digit = int(input("Please type count of digits: "))
pi = 1

for i in range(1, 100000000):
    pi += ((-1) ** i) * (1 / (2 * i +1))

result = pi * 4
print(round(result, digit))
Number_pi.py