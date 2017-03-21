/* flags.c – Source file */

#include <stdio.h>
#include "flags.h"
#include <stdlib.h>
#include "string.h"

int gFlag = 0;

void welcome_msg(char *msg) {
printf("%s\n", msg);
return;
}

int get_flag() {
return gFlag;
}

void set_flag(int flag) {
gFlag = flag;
return;
}
