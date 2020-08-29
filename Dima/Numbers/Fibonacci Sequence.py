print('Input number:')
n = int(input())


def Fib_num(n):
    i = 0
    f0 = 0
    f1 = 1
    fib = [0, 1]
    if n == 0:
        f1 = f0
        fib = []
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
    return fib

print("List of Fib:")
print(Fib_num(n))
