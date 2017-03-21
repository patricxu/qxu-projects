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
