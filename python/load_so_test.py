from ctypes import *
mylib = CDLL("/mnt/hgfs/vmshared/sample/c/libflags.so")
mylib.welcome_msg(b"Hi C, I am from Python!")
