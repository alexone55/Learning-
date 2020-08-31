n = int(input("Type number: "))
i = 2
factors = []

while i <= n:
    if n % i == 0:
        factors.append(i)
        n = n / i
    else:
        i = i + 1

print(*factors)



