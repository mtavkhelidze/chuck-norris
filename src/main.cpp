#include "chuck-fact.hpp"
#include <iostream>

int main()
{
    ChuckNorris cn;
    std::string fact = cn.get_fact();
    std::cout << fact << std::endl;
    return 0;
}
