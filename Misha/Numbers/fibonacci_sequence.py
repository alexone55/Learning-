def generate_sequence():
    num = int(input('Enter Nth number of Fibonacci sequence: '))
    sequence = [0, 1]
    for i in range(2, num):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    print('Sequence: ', end='')
    for i in range(num):
        print(sequence[i], end=' ')


if __name__ == "__main__":
    print('This program generate the Fibonacci sequence to the Nth number\n')
    generate_sequence()
