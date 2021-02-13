#include "../includes/tetravex.h"

int main(int argc, char * argv[]) {

    if (argc != 2) FATAL_ERROR("Test Main - A .tetra file was expected as argument.", 2);

    grid tetravex = read_grid(argv[1]);

    for(int square_i = 0; square_i < (tetravex.size * tetravex.size); square_i++) {
        debug_square(tetravex.tab[square_i], square_i);        
    }

    return 0;
}