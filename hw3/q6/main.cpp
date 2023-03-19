#include <iostream>
#include <stdio.h>
#include <limits>
#include <cmath>
using namespace std;







int main() {

    

    unsigned long remaining = 21;
    unsigned long goal = 13;

    unsigned long result = (~((remaining - goal) | 0));
    
    unsigned long shift = (((sizeof(unsigned long) * 8) - int(round(log2(remaining - goal)))));
    unsigned long t = result << shift;
    result = t >> shift;
    cout << result;
    return 1;
}