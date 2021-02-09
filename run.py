import threading


def fun(msg):
    print("Sending Message {}".format(msg))


if __name__ == '__main__':
    messages = ["Hello", "How are you", "You can ask anything to me"]

    wait_time = 0.0  # in second
    for message in messages:
        timer = threading.Timer(wait_time, fun, [message])
        timer.start()
        wait_time = len(message)

