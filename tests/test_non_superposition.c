#include "../includes/logic.h"

int main(int argc, char * argv[]) {
    //> Check number of argument
    if (argc != 3) FATAL_ERROR("Test Main - A .tetra file and a result file were expected as arguments.", 2);

    //> Read the grid from the given file
    grid tetravex = read_grid(argv[1]);

    //> Test the coord unicity function
    FILE * filepointer = fopen(argv[2], "w");
    non_superposition(tetravex, filepointer);
    fclose(filepointer);

    return 0;
}