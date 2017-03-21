#import sys
#sys.path.append('/')
#sys.path.append('/root/anaconda3/lib/python3.5/ctypes')
from ctypes import *  
  
#python中结构体定义  
class Block(Structure):  
    _fields_ = [("name", c_char * 20), ("age", c_int)]  
  
if __name__ == "__main__":  
    lib = cdll.LoadLibrary("./libtest.so")  
    lib.test.restype = POINTER(Block)  
    p = lib.test()  
  
    print ("%s: %d" %(p.contents.name, p.contents.age)) 

#使用byref(structure_obj)获取指向obj的指针