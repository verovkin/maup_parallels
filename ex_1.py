import threading
import time
import random


class NewThread(threading.Thread):
    def __init__(self, thread_number):
        threading.Thread.__init__(self)
        self.name = "Thread #%s" % (thread_number + 1)
        self.interval = random.randint(3, 15)
        self.start()

    def run(self):
        time.sleep(self.interval)
        print("%s is running\n" % self.name)


def create_threads(thread_number):
    NewThread(thread_number)


if __name__ == '__main__':
    for i in range(5):
        create_threads(i)
