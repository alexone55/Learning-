def generate_next_value(number_1,number_2,sequence,n_number):
    next_number = number_1 + number_2
    sequence.append(next_number)
    if len(sequence)<n_number:
        generate_next_value(number_2,next_number,sequence,n_number)


def main():
    print('This program generate fibonacci sequence to the Nth digit')
    n_number = int(input('Enter Nth number of Fibonacci sequence: '))
    sequence = [0, 1]
    generate_next_value(sequence[0], sequence[1], sequence, n_number)
    print('Sequence:',end=' ')
    for index in range(n_number):
        print(sequence[index],end=' ')


if __name__=="__main__":
    main()