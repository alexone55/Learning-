import random
import time


def simulate_coin_flips(number_of_flips):
    random.seed(time.time())
    tails = 0
    heads = 0
    for index in range(number_of_flips):
        flip = random.randint(0,1)
        if flip == 1:
            heads += 1
        elif flip == 0:
            tails += 1
    return tails, heads


def main():
    print('This program is a coin flip simulator and it shows statistics about flips')
    number_of_flips = int(input('Enter number of flips: '))
    tails, heads = simulate_coin_flips(number_of_flips)
    percent_of_tails = round(float(tails * 100 / number_of_flips), 2)
    percent_of_heads = round(100 - percent_of_tails, 2)
    print('Tails: ' + str(percent_of_tails))
    print('Heads: ' + str(percent_of_heads))


if __name__ == "__main__":
    main()
