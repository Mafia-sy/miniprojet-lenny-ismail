// test2.cpp
#include "hello.h"
#include <cassert>

std::string hello(const std::string& name);

void test_hello() {
    assert(hello("World") == "Hello, World!"); // Test qui réussit
    //assert(hello("GitLab") == "Hello, Test!"); // Test qui échoue intentionnellement
}

int main() {
    test_hello();
    std::cout << "Test 2 passed!!aa!" << std::endl;
    return 0; // Si l'un des tests échoue, cela ne sera pas atteint
}
