import time


def main():
    print("What time do you want to wake up?")
    print("Use this form.\nExample: 06:30:00")
    alarm = input(">")
    clock(alarm)


def clock(alarm):
    now_time = time.strftime("%H:%M:%S")
    while time != alarm:
        now_time = time.strftime("%H:%M:%S")
        print("The time is: " + now_time)
        time.sleep(1)

        if now_time == alarm:
            print("Time to wake up! Time to wake up! Time to wake up!")
            break


if __name__ == '__main__':
    main()
