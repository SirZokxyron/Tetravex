#ifndef _BOOLEAN_H_
#define _BOOLEAN_H_

#include "../includes/types_macro.h"

/* Data structures */

    //* Creating an alias for int as expression
    typedef int expression;

/* Functions */

    //* Return negative of an expression
    expression neg(expression e);

    //* Combine a given string with a given expression
    string concat_exp(string str, expression exp);

#endif