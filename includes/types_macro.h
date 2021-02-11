#ifndef _TYPES_MACRO_H_
#define _TYPES_MACRO_H_

#include <stdio.h>      //> Get basic C functions
#include <stdlib.h>     //> Get the malloc function
#include <string.h>     //> Get all the string related functions
#include <stdbool.h>    //> Get the bool type (int) and (true, false) value

//> Creating an alias for char * as string
typedef char * string;

//> Macro displaying an error message before returning the given error code
#define FATAL_ERROR(_m_, _c_) \
{ \
fprintf(stderr, "%s\n", _m_); \
exit(_c_); \
}

#endif