import time


def main():
    print('This program is a timer that shows message after X seconds')
    amount_of_seconds=int(input('Enter the amount of seconds: '))
    time.sleep(amount_of_seconds)
    print(str(amount_of_seconds) + ' second(s) passed. It\'s time to do something!')

if __name__=="__main__":
    main()