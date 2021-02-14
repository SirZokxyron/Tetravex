#include "../includes/boolean.h"

//* Return negative of an expression
expression neg(expression e) {
    return -e;
}

//* Combine a given string with a given expression
string concat_exp(string str, expression exp) {
    string new_str;
    if (strlen(str) == 0) {
        new_str = (string)malloc(7);
        sprintf(new_str, "%d", exp);
    }    
    else if (!exp) {
        new_str = (string)malloc(strlen(str) + 7);
        sprintf(new_str, "%s %d\n", str, exp);
    } else {
        new_str = (string)malloc(strlen(str) + 6);
        sprintf(new_str, "%s %d", str, exp);
    }
    return new_str;
}