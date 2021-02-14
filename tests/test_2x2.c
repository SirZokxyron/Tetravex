#include "../includes/tetravex.h"

int main(int argc, char * argv[]) {
    //> Check number of argument
    if (argc != 2) FATAL_ERROR("Test Main - A .tetra file was expected as argument.", 2);

    //> Read the grid from the given file
    grid tetravex = read_grid(argv[1]);

    //> Debug the grid and square content
    for(int square_i = 0; square_i < (tetravex.size * tetravex.size); square_i++) {
        debug_square(tetravex, tetravex.tab[square_i], square_i);        
    }

    return 0;
}