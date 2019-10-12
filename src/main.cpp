#include "chuck-fact.hpp"
#include <iostream>

int main()
{
    ChuckNorrisFact cn;
    std::string fact = cn.get();
    std::cout << fact << std::endl;
    return 0;
}
