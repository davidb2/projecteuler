#include <iostream>
#include <cmath>

#define LIMIT pow(10, 12)

int main() {
    for (long i = 1; i <= LIMIT; i++) {
        if (i % 100000000 == 0) {
            std::cout << i << std::endl;
        }
    }
}