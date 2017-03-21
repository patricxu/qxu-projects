def fun():
    try:
        fun.cb()
    except:
        print("hello")

def fun2():
    print("world")

fun.cb=fun2
fun()

