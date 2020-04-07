import threading
from time import sleep

respList = []


class forThread(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.name = 'myThread'
        self.event = event

    def run(self):
        sleep(5)
        #print(self.event)
        print(self.event.get('a'))
        respList.append({'xxx': self.event})


if __name__ == '__main__':
    i = 1
    input_data = [
        {'a': 1, 'b': 2, 'c': 3}
        , {'a': 1, 'b': 2, 'c': 3}
        , {'a': 1, 'b': 2, 'c': 3}
    ]
    respList = []
    for line in input_data:
        #print(line)
        #print(i)
        data = line
        exec('thread{} = forThread(data)'.format(i))
        exec('thread{}.start()'.format(i))
        i += 1

    # i = 1
    # for line in eventList:
    #     #print(line)
    #     #print(i)
    #     exec('thread{}.join()'.format(i))
    #     i += 1

    x = 1
    while x < i :
        exec('thread{}.join()'.format(x))
        x += 1

    print(respList)
    # print('var1 = ' + str(thread1))

    #     thread = forThread(line)
    #     thread.start()
    #
    # for line in eventList:
    #     thread.join()
    # thread1 = forThread(eventList[0])
    # thread2 = forThread(eventList[1])
    # thread3 = forThread(eventList[2])
    #
    # thread1.start()
    # thread2.start()
    # thread3.start()
    #
    # thread1.join()
    # thread2.join()
    # thread3.join()

