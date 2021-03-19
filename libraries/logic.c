#include "../includes/logic.h"

//TODO: Initialize one clause
clause * init_clause(int size) {
    clause * cell;
    cell = (clause *)malloc(sizeof(clause));
    cell->tab = (int *)malloc(size);
    cell->size_tab = 0;
    cell->next = NULL;
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
    cell->next = env->first;
    env->size++;
    env->first = cell;
}

//TODO: Printing cell
void print_clause(clause * cell) {
    for(int i = 0; i < cell->size_tab; i++) {
        printf("%d ", cell->tab[i]);
    }
    printf("0\n");
}

//TODO: Printing cnf_env
void print_env(cnf_env env) {
    clause * cell;
    cell = env.first;
    for(int i = 0; i < env.size; i++) {
        print_clause(cell);
        cell = cell->next;
    }
}

//TODO: Concatenate two cnf_env
void concat_env(cnf_env * env1, cnf_env * env2) {
    env1->size += env2->size;

    clause * p;
    p = env1->first;
    while(p->next) p = p->next;
    p->next = env2->first;
}

cnf_env coord_unicity(grid tetravex) {
    int n = tetravex.size;
    cnf_env env = init_env();
    for(int square_i = 0; square_i < (n * n); square_i++) {
        clause * coord_x = init_clause(n);
        clause * coord_y = init_clause(n);

        for(int coord_i = 0; coord_i < n; coord_i++) {
            add_to_clause(coord_x, tetravex.tab[square_i].bool_x[coord_i]);
            add_to_clause(coord_y, tetravex.tab[square_i].bool_y[coord_i]);

            for(int coord_i_n = coord_i + 1; coord_i_n < n; coord_i_n++) {
                clause * coord_x_neg = init_clause(n);
                clause * coord_y_neg = init_clause(n);

                add_to_clause(coord_x_neg, -(tetravex.tab[square_i].bool_x[coord_i]));
                add_to_clause(coord_y_neg, -(tetravex.tab[square_i].bool_y[coord_i]));
                add_to_clause(coord_x_neg, -(tetravex.tab[square_i].bool_x[coord_i_n]));
                add_to_clause(coord_y_neg, -(tetravex.tab[square_i].bool_y[coord_i_n]));

                add_to_env(&env, coord_x_neg);
                add_to_env(&env, coord_y_neg);
            }
        }
        add_to_env(&env, coord_x);
        add_to_env(&env, coord_y);
    }
    return env;
}

cnf_env non_superposition(grid tetravex) {
    int n = tetravex.size;
    cnf_env env = init_env();

    for(int square_i = 0; square_i < (n * n); square_i++) {
        for(int square_i_p = square_i + 1; square_i_p < (n * n); square_i_p++) {
            for(int i = 0; i < n; i++) {
                for(int j = 0; j < n; j++) {
                    clause * clause_x = init_clause(4);
                    clause * clause_x_p = init_clause(4);
                    clause * clause_y = init_clause(4);
                    clause * clause_y_p = init_clause(4);

                    add_to_clause(clause_x, -(tetravex.tab[square_i].bool_x[i]));
                    add_to_clause(clause_x, -(tetravex.tab[square_i_p].bool_x[i]));
                    add_to_clause(clause_x_p, -(tetravex.tab[square_i_p].bool_x[i]));
                    add_to_clause(clause_x_p, -(tetravex.tab[square_i].bool_x[i]));
                    add_to_clause(clause_y, -(tetravex.tab[square_i].bool_y[i]));
                    add_to_clause(clause_y, -(tetravex.tab[square_i_p].bool_y[i]));
                    add_to_clause(clause_y_p, -(tetravex.tab[square_i_p].bool_y[i]));
                    add_to_clause(clause_y_p, -(tetravex.tab[square_i].bool_y[i]));

                    add_to_clause(clause_x, -(tetravex.tab[square_i].bool_y[j]));
                    add_to_clause(clause_x, -(tetravex.tab[square_i_p].bool_y[j]));
                    add_to_clause(clause_x_p, -(tetravex.tab[square_i].bool_y[j]));
                    add_to_clause(clause_x_p, -(tetravex.tab[square_i_p].bool_y[j]));
                    add_to_clause(clause_y, -(tetravex.tab[square_i].bool_x[j]));
                    add_to_clause(clause_y, -(tetravex.tab[square_i_p].bool_x[j]));
                    add_to_clause(clause_y_p, -(tetravex.tab[square_i].bool_x[j]));
                    add_to_clause(clause_y_p, -(tetravex.tab[square_i_p].bool_x[j]));

                    add_to_env(&env, clause_x);
                    add_to_env(&env, clause_x_p);
                    add_to_env(&env, clause_y);
                    add_to_env(&env, clause_y_p);
                }
            }
        }
    }

    return env;
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