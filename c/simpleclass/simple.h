#include <stdio.h>
#include <iostream>
#include <string.h>

class MyClass
{
private:
	int m_i;
	std::string m_str;
	MyClass();
public:

	MyClass(std::string str);

	~MyClass();
};
