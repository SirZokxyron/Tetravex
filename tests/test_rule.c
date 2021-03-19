#include "../includes/logic.h"

int main(int argc, string argv[]) {

    //> Check number of argument
    if (argc != 2) FATAL_ERROR("Test Main - A .tetra file was expected as argument.", 2);

    //> Read the grid from the given file
    grid tetravex = read_grid(argv[1]);

    cnf_env env1 = coord_unicity(tetravex);
    // cnf_env env2 = non_superposition(tetravex);

    // concat_env(&env1, &env2);

    print_env(env1);

    return 0;
}