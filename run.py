import threading


def fun():
    print("Invoke API")


if __name__ == '__main__':
    wait_time = 5.0 #in second
    timer = threading.Timer(wait_time, fun)
    timer.start()
    print("Exit")

