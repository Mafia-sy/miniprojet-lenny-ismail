// hello.cpp
#include "hello.h"
#include <string>
std::string hello(const std::string& name) {
	std::string strRet = "Hello, " + name + "!";
	std::cout << strRet << std::endl;	
      	return strRet;
}
