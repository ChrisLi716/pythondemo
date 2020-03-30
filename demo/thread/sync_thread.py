import threading
import time

lst = []


class SyncThread(threading.Thread):
    thread_lock = threading.Lock()

    def __init__(self, thread_id, name):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name

    def run(self):
        self.thread_lock.acquire()
        thread_name = self.getName()
        print("lock " + thread_name)

        for i in range(20):
            self.print_list(thread_name)
            self.set_lst(self.thread_id)

        self.thread_lock.release()
        print("unlock " + thread_name)

    @staticmethod
    def print_list(thread_name):
        print(thread_name, lst, sep="|")

    @staticmethod
    def set_lst(val):
        lst.clear()
        for i in range(10):
            lst.append(val)


if __name__ == '__main__':
    thread1 = SyncThread(1, "thread_1")
    thread2 = SyncThread(2, "thread_2")

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    time.sleep(60)
