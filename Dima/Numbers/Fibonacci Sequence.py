n = int(input())
f0 = 0
f1 = 1
i = 0

fib = [0, 1]
if n == 0:
    f1 = f0
while i <= n:
    fi = f0 + f1
    if fi == n:
        fib.append(fi)
        break
    else:
        f0 = f1
        f1 = fi
        fib.append(fi)
        i += 1

print("List of Fib:")
print(*fib)
