#include "../includes/logic.h"

int main() {

    //initialisation clauses + environnement
    clause * clause1 = init_clause(3);

    cnf_env env1 = init_env();

    //ajouter int dans clause
    add_to_clause(clause1, 1);
    add_to_clause(clause1, -2);
    add_to_clause(clause1, 3);

    add_to_env(&env1, clause1);

    clause1 = init_clause(3);

    add_to_clause(clause1, 1);
    add_to_clause(clause1, -2);
    add_to_clause(clause1, 3);

    add_to_env(&env1, clause1);

    print_env(env1);

    return 0;
}