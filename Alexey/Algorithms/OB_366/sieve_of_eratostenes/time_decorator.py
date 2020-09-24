def timer(function):
    import time

    def start_to_finish_time(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        print('Время выполнения: {} секунд.'.format(end_time - start_time))
        return result
    return start_to_finish_time


if __name__ == "__main__":
    timer()

