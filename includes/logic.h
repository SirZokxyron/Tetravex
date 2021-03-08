#ifndef _LOGIC_H_
#define _LOGIC_H_

#include "../includes/tetravex.h"

/* Data structures */

    //* Structure essentially representing one clause of int
    typedef struct clause_ {
        //TODO: Data structure to hold one clause
    } clause;

    //* Structure essentially representing all of our clauses
    typedef struct cnf_env_ {
        //TODO: Data structure to hold many clauses
    } cnf_env;

/* Functions */

    //TODO: Initialize one clause
    //! This function may be useless of the clause doesn't require it, the coder knows best

    //TODO: Modify one clause (add an int to the clause)

    //TODO: Initialize one cnf_env
    //! This function is mandatory as the number of clause will always be the same depending of the grid size

    //TODO: Modify one cnf_env (add a clause to the cnf_env)

    //TODO: Output a given cnf_env to a DIMACS file
    //! DIMACS format:
    //> p cnf [n literals] [n clauses]
    //> [clause 1] 0
    //> ... 0
    //> [clause n] 0 

#endif