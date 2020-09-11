import random


def main():
    answer = input("Flip a coin?: y/n ")
    if answer.lower() == "y":

        random_number = random.randint(0, 1)
        flip_simulator(random_number)
    else:
        pass


def flip_simulator(count_of_flips, tails=0, heads=0):
    print("Count of heads is: " + str(int(heads)))
    if count_of_flips % 2 == 0:
        print("Count of tails is: " + str(int(tails)))
        print("Tails")
        tails += 1
    else:
        print("Count of tails is: " + str(int(tails)))
        print("Heads")
        heads += 1
    second_answer = input("Do it again? ")

    if second_answer.lower() == "y":
        random_number = random.randint(0, 1)
        flip_simulator(random_number, tails, heads)
    else:
        pass



if __name__ == '__main__':
    main()

