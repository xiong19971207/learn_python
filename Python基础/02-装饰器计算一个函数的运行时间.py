import time


def cal(fn):
    print('cal被调用了')

    def wrapper():
        start = time.time()
        fn()
        end = time.time()
        print('被装饰的函数运行了%f秒' % (end - start))

    return wrapper


@cal
def _fun():
    for i in range(10000):
        print('Hello World!')


print(_fun)
