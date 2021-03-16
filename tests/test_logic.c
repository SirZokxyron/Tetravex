#include "../includes/logic.h"

int main() {

    //initialisation clauses + environnement
    clause * clause1 = init_clause(3);
    clause * clause2 = init_clause(3);

    cnf_env env = init_env();

    //ajouter int dans clause
    add_to_clause(clause1, 1);
    add_to_clause(clause1, -2);
    add_to_clause(clause1, 3);
    
    add_to_clause(clause2, 1);
    add_to_clause(clause2, -5);
    add_to_clause(clause2, 7);

    add_to_env(&env, clause1);
    add_to_env(&env, clause2);
    
    print_env(env);

    return 0;
}