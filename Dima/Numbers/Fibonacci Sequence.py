<<<<<<< HEAD
def fibonacci(n):
    i = 0
    previous_fib_num = 0
    now_fib_num = 1
    fibonacci_sequence = [0, 1]
    ans = 'Number N - isn`t in Fibonacci sequence, here is Fibonacci sequence to N`th number: '
    if n == 0:
        now_fib_num = previous_fib_num
        fibonacci_sequence = []
    while i <= n:
        fi = previous_fib_num + now_fib_num
        if fi == n:
            fibonacci_sequence.append(fi)
            ans = 'Number N is in the Fibonacci sequence: '
            break
        else:
            previous_fib_num = now_fib_num
            now_fib_num = fi
            fibonacci_sequence.append(fi)
            i += 1
    return ans, fibonacci_sequence


def main():
    n = int(input("Enter the number 'N': "))
    answer, fibonacci_sequence = fibonacci(n)
    print(answer, *fibonacci_sequence)


if __name__ == "__main__":
    main()
=======
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
>>>>>>> parent of 7fb3b86... Update Fibonacci Sequence.py
