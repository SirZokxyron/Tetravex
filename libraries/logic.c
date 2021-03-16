#include "../includes/logic.h"

//TODO: Initialize one clause
clause * init_clause(int size) {
    clause * cell;
    cell = (clause *)malloc(sizeof(clause));
    cell->tab = (int *)malloc(size);
    cell->size_tab = 0;
    cell->suivant = NULL;
    return cell;
}

//TODO: Modify one clause (add an int to the clause)
void add_to_clause(clause * cell, int e) {
    cell->tab[cell->size_tab] = e;
    cell->size_tab++;
}

//TODO: Initialize one cnf_env
cnf_env init_env() {
    cnf_env env;
    env.size = 0;
    env.first = NULL;
    return env;
}

//TODO: Modify one cnf_env (add a clause to the cnf_env)
void add_to_env(cnf_env * env, clause * cell) {
    cell->suivant = env->first;
    env->size++;
    env->first = cell;
}

//TODO: Printing cell
void print_clause(clause * cell) {
    for(int i = 0; i < cell->size_tab; i++) {
        printf("%d ", cell->tab[i]);
    }
    printf("\n");
}

//TODO: Printing cnf_env
void print_env(cnf_env env) {
    clause * cell;
    cell = env.first;
    for(int i = 0; i < env.size; i++) {
        print_clause(cell);
        cell = cell->suivant;
    }
    printf("\n");
}

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