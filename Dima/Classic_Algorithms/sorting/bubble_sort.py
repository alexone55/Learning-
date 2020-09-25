from Dima.Decorators.time_decorator import timer
import random


def bubble_sort(our_list):
    try:
        for i in range(len(our_list)):
            for j in range(len(our_list) - 1):
                if our_list[j] > our_list[j+1]:
                    our_list[j], our_list[j+1] = our_list[j+1], our_list[j]
        return our_list
    except TypeError:
        raise TypeError('TypeError')


@timer
def main():
    random_list = random.sample(range(0, 1000), 1000)
    print('Random list: ', *random_list)
    print('Sorted list: ', *bubble_sort(random_list))


if __name__ == "__main__":
    main()
