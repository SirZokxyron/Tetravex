#include "../includes/logic.h"

int main(int argc, char * argv[]) {
    //> Check number of argument
    if (argc != 2) FATAL_ERROR("Test Main - A .tetra file was expected as argument.", 2);

    //> Read the grid from the given file
    grid tetravex = read_grid(argv[1]);

    //> Test the coord unicity function
    FILE * filepointer = fopen("test", "w");
    coord_unicity(tetravex, filepointer);
    fclose(filepointer);

    return 0;
}