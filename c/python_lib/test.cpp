// 编译生成动态库: gcc -g -fPIC -shared -o libtest.so test.c  
  
#include <stdio.h>  
#include <string.h>  
#include <stdlib.h>  

  
typedef struct StructPointerTest  
{  
    char name[20];  
    int age;  
}StructPointerTest, *StructPointer;  
  
extern "C" StructPointer test()    // 返回结构体指针  
{   
    StructPointer p = (StructPointer)malloc(sizeof(StructPointerTest));   
    strcpy(p->name, "Joe");  
    p->age = 20;  
      
    return p;   
}

typedef struct StructPointerTest2
{
    float* ptr;
    int len;
}StructPointerTest2, *StructPointer2;

extern "C" StructPointer2 test2()    // 返回结构体指针  
{
    StructPointer2 p = (StructPointer2)malloc(sizeof(StructPointerTest2));
    p->ptr = (float*)malloc(16);
    memset(p->ptr, 0, 16);
    p->ptr[0] = 1.5;
    p->ptr[1] = 2;
//    memset(p->ptr, 0xff, 16);
    p->len = 2;

    return p;
}
  
  
