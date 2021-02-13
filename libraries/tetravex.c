#include "../includes/tetravex.h"

//* Returns a grid with the correct given size and allocates the memory for the square array
grid init_grid(int size) {
    //> Create the new grid
    grid new_grid;

    //> Update the size
    new_grid.size = size;

    //> Allocates the right amount of square memory in the array
    new_grid.tab = (square *)malloc(size * sizeof(square));

    return new_grid;
}

//* Returns a square with the correct given numbers around it and allocates the memory for every boolean array
square init_square(grid tetravex, int number_up, int number_right, int number_down, int number_left) {
    //> Create the new square    
    square new_square;

    //> Update the numbers around the square
    new_square.number_up = number_up;
    new_square.number_right = number_right;
    new_square.number_down = number_down;
    new_square.number_left = number_left;
    
    //> Allocates the right amount of expression memory
    new_square.bool_x = (expression *)malloc(tetravex.size * sizeof(expression));
    new_square.bool_y = (expression *)malloc(tetravex.size * sizeof(expression));
    
    return new_square;
}

//? Debug function to print out square parameters
void debug_square(square piece, int name) {
    printf("square %d :\n", name);
    printf("  %d  \n", piece.number_up);
    printf(" %d %d \n", piece.number_left, piece.number_right);
    printf("  %d  \n", piece.number_down);
}

//* Reads a given file to init a grid with squares inside
grid read_grid(string filename) {
    FILE * file_pointer;
    file_pointer = fopen(filename, "r");

    if (!file_pointer) FATAL_ERROR("read_grid - File was not found.", 1);
    
    int code;

    int size;
    code = fscanf(file_pointer, "%d", &size); 
    if (code != 1) FATAL_ERROR("read_grid - Size format issue in given file.", 1);
    grid new_grid = init_grid(size);

    expression literal = 1;

    for(int square_i = 0; square_i < new_grid.size; square_i++) {
        
        int up, right, down, left;
        code = fscanf(file_pointer, "%d ", &up); 
        if (code != 1) FATAL_ERROR("read_grid - Top number format issue in given file.", 1);
        code = fscanf(file_pointer, "%d ", &right); 
        if (code != 1) FATAL_ERROR("read_grid - Right number format issue in given file.", 1);
        code = fscanf(file_pointer, "%d ", &down); 
        if (code != 1) FATAL_ERROR("read_grid - Down number format issue in given file.", 1);
        code = fscanf(file_pointer, "%d\n", &left); 
        if (code != 1) FATAL_ERROR("read_grid - Left number format issue in given file.", 1);

        square new_square = init_square(new_grid, up, right, down, left);

        for (int i = 0; i < (new_grid.size * new_grid.size); i++) {
            new_square.bool_x[i] = literal;
            literal++;
            new_square.bool_y[i] = literal;
            literal++;
        }

        new_grid.tab[square_i] = new_square;
    }

    return new_grid;
}