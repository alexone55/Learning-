import random


def main():
    answer = input("Flip a coin?: y/n ")
    if answer.lower() == "y":

        random_number = random.randint(1, 100)
        flip_simulator(random_number)
        main()
    else:
        pass


def flip_simulator(count_of_flips):
    count_of_heads = count_of_flips / 2
    print("Count of heads is: " + str(int(count_of_heads)))
    if count_of_flips % 2 == 0:
        print("Count of tails is: " + str(int(count_of_heads)))
        print("Tails")
    else:
        print("Count of tails is: " + str(int(count_of_heads) + 1))
        print("Heads")


if __name__ == '__main__':
    main()

