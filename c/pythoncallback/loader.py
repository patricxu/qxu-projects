from ctypes import *

def callback(x):
    print("in python callback")
    print(x)
    return 0

#the first param of CFUNCTYPE is the return value
CMPFUNC = CFUNCTYPE(c_int, c_char_p)
_callback = CMPFUNC(callback)

somlib = CDLL("./libsome.so")

res = somlib.DllTestCB(_callback, b"call dlltestcb")