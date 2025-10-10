// test1.cpp
#include "hello.h"
#include <cassert>


std::string hello(const std::string& name);

void test_hello() {
    assert(hello("World") == "Hello, World!"); // Test qui réussit
    assert(hello("GitLab") == "Hello, GitLab!"); // Test qui réussit
}

int main() {
    test_hello();
    std::cout << "Test 1 passed!!!" << std::endl;
    return 0; // Indique que le test a réussi
}
