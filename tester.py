def fun1():
    print('Hello from fun1()')


def fun2():
    print('Hello from fun2()')


def main():
    fun1()
    fun2()
    fun1()
    fun2()
    for i in range(10):
        fun1()
        fun2()


main()
