#include <stdio.h>  
#include <stdlib.h>  
#include <math.h>  
  
#define MAX_INPUT 25  

double sin(double x);
float sinf(float x);
long double sinl(long double x);
  
int main(int agrc, char **argv)  
{  
        char input[MAX_INPUT];  
        double angle;  
  
        printf("Give me an angle (in radians) ==>");  
        if(!fgets(input, MAX_INPUT, stdin)){  
                perror("an error occurred.\n");  
        }  
        angle = strtod(input, NULL);  
  
        printf("sin(%e) = %e\n", angle, sin(angle));  
  
        return 0;  
}  
