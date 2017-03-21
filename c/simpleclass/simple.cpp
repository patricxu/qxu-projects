#include "simple.h"

MyClass::MyClass():m_i(0),m_str("abc")
{

}

MyClass::MyClass(std::string str):m_i(1),m_str(str)
{

}

MyClass::~MyClass()
{

}
