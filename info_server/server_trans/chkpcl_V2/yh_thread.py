import threading
import time


# class MyThread(threading.Thread):
#     """
#     使用继承的方式实现多线程
#     """
#     def __init__(self, who):
#         super().__init__()    # 必须调用父类的构造方法
#         self.name = who
#
#     def run(self):
#         print("%s is run..." % self.name)
#         time.sleep(3)
#
# if __name__ == "__main__":
#     # t1 = MyThread("Jet")    # 创建线程1
#     # t2 = MyThread("Jack")   # 创建线程2
#     # t1.start()              # 运行线程1
#     # t2.start()              # 运行线程2
#     # print("over...")
#     threads=[]
#     thread_list = ['aaa', 'bbb', 'ccc', 'ddd']
#     for line in thread_list:
#         t = threading.Thread(line)
#         threads.append(t)
#     # for msg in threads:


# import threading
# from datetime import datetime
# import time
#
# def thread_func():  # 线程函数
#     time.sleep(2)
#     print('我是一个线程函数',threading.current_thread().getName(), datetime.now())
#
# def many_thread():
#     threads = []
#     # for _ in range(10):  # 循环创建10个线程
#     thread_list=['aaa','bbb','ccc','ddd']
#     for i in thread_list:
#         t = threading.Thread(name=i,target=thread_func)
#         threads.append(t)
#     for t in threads:  # 循环启动10个线程
#         t.start()
#     for t in threads:  # 循环启动10个线程
#         t.join()
#
# if __name__ == '__main__':
#     start = datetime.today().now()
#     many_thread()
#     duration = datetime.today().now() - start
#     print("耗时:",duration)

# ----------------------------------------------------------------------------------------------------
# import threading
# from datetime import datetime
# import time
# def thread_func():  # 线程函数
#     time.sleep(2)
#     print('我是一个线程函数', threading.current_thread().name,datetime.now())
# def many_thread():
#     threads = []
#     for _ in range(1000):  # 循环创建500个线程
#         t = threading.Thread(target=thread_func)
#         threads.append(t)
#     for t in threads:  # 循环启动500个线程
#         t.start()
#     for t in threads:  # 循环启动500个线程
#         t.join()
# if __name__ == '__main__':
#     start = datetime.today().now()
#     many_thread()
#     duration = datetime.today().now() - start
#     print(duration)




# import threading
# from datetime import datetime
# import time
# def thread_func(): # 线程函数
#     print('我是一个线程函数',threading.current_thread().name, datetime.now())
#     time.sleep(10)
#
# def execute_func():
#     for _ in range(2):
#         thread_func()
# def many_thread():
#     start = datetime.now()
#     threads = []
#     for key in range(3): # 循环创建500个线程
#         t = threading.Thread(target=execute_func)
#         threads.append(t)
#         t.setDaemon(True)  # 给每个子线程添加守护线程
#     for t in threads: # 循环启动500个线程
#         t.start()
#     for t in threads: # 循环启动500个线程
#         t.join()     #设置抑制退出
#
# if __name__ == '__main__':
#     start = datetime.today().now()
#     many_thread()
#     duration = datetime.now() - start
#     print("耗时:",duration)



# import threading
# from datetime import datetime
# import time
# def thread_func(): # 线程函数
#     time.sleep(5)
#     i = 0
#     while(i < 3):
#         print(datetime.now())
#         i += 1
# def many_thread():
#     threads = []
#     for _ in range(10): # 循环创建500个线程
#         t = threading.Thread(target=thread_func)
#         threads.append(t)
#     for t in threads: # 循环启动500个线程
#         t.start()
# if __name__ == '__main__':
#     many_thread()
#     print("thread end")


# import threading
# from datetime import datetime
# import time
# def thread_func():  # 线程函数
#     i = 0
#     while (1):
#         print(datetime.now())
#         i += 1
#
# def many_thread():
#     threads = []
#     for _ in range(3):  # 循环创建500个线程
#         t = threading.Thread(target=thread_func)
#         threads.append(t)
#         t.setDaemon(True)  # 给每个子线程添加守护线程
#     for t in threads:  # 循环启动500个线程
#         t.start()
#     for t in threads:  # 循环启动500个线程
#         t.join(2)
#
# if __name__ == '__main__':
#     many_thread()
#     print("thread end")



# import threading
# from datetime import datetime
# import time
# def thread_func(): # 线程函数
#     time.sleep(1)
#     i = 0
#     while(1):
#         print(datetime.now())
#         i += 1
# def many_thread():
#     threads = []
#     for _ in range(1): # 循环创建500个线程
#         t = threading.Thread(target=thread_func)
#         threads.append(t)
#         t.setDaemon(True) # 给每个子线程添加守护线程
#     for t in threads: # 循环启动500个线程
#         t.start()
#     for t in threads:
#         t.join(2) # 设置子线程超时2秒
# if __name__ == '__main__':
#     many_thread()
#     print("thread end")