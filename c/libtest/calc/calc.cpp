#include "calc.h"

#include "add.h"

#include "sub.h"

#include <stdio.h>

void func(int a, int b)

{

    int result = add(a,b);

    printf("%d+%d=%d\n",a, b, result);

    result = sub(a,b);

    printf("%d-%d=%d\n",a, b, result);

}
