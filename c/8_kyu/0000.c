// solution L1: Set Alarm
// https://www.codewars.com/kata/568dcc3c7f12767a62000038/solutions/c

#include <stdbool.h>
#include <stdlib.h>

bool set_alarm(bool employed, bool vacation) {

    // if (employed && vacation == false) 
    // {
    //     return true;
    // }

    return employed  == true && vacation == false;
}

