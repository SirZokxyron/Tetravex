#ifndef _LOGIC_H_
#define _LOGIC_H_

#include "../includes/tetravex.h"

/* Data structures */

    //* Structure essentially representing one clause of int
    typedef struct clause_ {
        //TODO: Data structure to hold one clause
        int size_tab;
        int * tab;
        struct clause_ * suivant;
    } clause;

    //* Structure essentially representing all of our clauses
    typedef struct cnf_env_ {
        //TODO: Data structure to hold many clauses
        int size;
        clause * first;
    } cnf_env;

/* Functions */

    //TODO: Initialize one clause
    clause * init_clause(int size);

    //TODO: Modify one clause (add an int to the clause)
    void add_to_clause(clause * cell, int e);

    //TODO: Initialize one cnf_env
    cnf_env init_env();

    //TODO: Modify one cnf_env (add a clause to the cnf_env)
    void add_to_env(cnf_env * env, clause * cell);

    //TODO: Printing cell
    void print_clause(clause * cell);

    //TODO: Printing cnf_env
    void print_env(cnf_env env);

    //TODO: Output a given cnf_env to a DIMACS file
    //! DIMACS format:
    //> p cnf [n literals] [n clauses]
    //> [clause 1] 0
    //> ... 0
    //> [clause n] 0

    //TODO: Get output of sat4j SAT-Solver
    //> Output SAT-Solver to file
    //>     sat4j sample.cnf > result.solve
    //> Check if "SATISFIABLE" or "UNSATISFIABLE"
    //>     cat result.solve | grep "SATIS" | cut -d" " -f2 
    //> if "SATISFIABLE" then
    //>     cat result.solve | grep "v "

#endif