import threading


def gfg():
    print("Invoke API")


if __name__ == '__main__':
    timer = threading.Timer(5.0, gfg)
    timer.start()
    print("Exit\n")

