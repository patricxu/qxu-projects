import time, threading

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread())
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread(), n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread())

print('thread %s is running...' % threading.current_thread())
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread())