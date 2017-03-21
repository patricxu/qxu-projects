#include <stdio.h>

int global_var = 1;
int global_var2;

void Print()
{
	printf("hello linux");
}

class Obj
{
private:
	int m;
public:
	Obj(int x):m(x){};
	Obj():m(0){};
};

int main()
{
	int local_var;
	Print();

	Obj o;
	return 0;
}
