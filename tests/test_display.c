#include "../includes/tetravex.h"

int main(int argc, char * argv[]) {
    //> Check number of argument
    if (argc != 3) FATAL_ERROR("Test Main - A .tetra file and a debug mode (0-1) were expected as arguments.", 2);

    //> Read the grid from the given file
    grid tetravex = read_grid(argv[1]);

    switch (atoi(argv[2])) {
        case 1:
            for(int square_i = 0; square_i < (tetravex.size * tetravex.size); square_i++) {
                debug_square(tetravex, tetravex.tab[square_i], square_i); 
            }
            break;
        case 0:
        default:
            print_grid(tetravex);
            break;
    }

    return 0;
}