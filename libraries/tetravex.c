#include "../includes/tetravex.h"

//* Returns a grid with the correct given size and allocates the memory for the square array
grid init_grid(int size) {
    //> Create the new grid
    grid new_grid;

    //> Update the size
    new_grid.size = size;

    //> Allocates the right amount of square memory in the array
    new_grid.tab = (square *)malloc((size * size) * sizeof(square));

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
void debug_square(grid tetravex, square piece, int name) {
    printf("square %d :\n", name);
    printf(" bool_x : ");
    for(int x_i = 0; x_i < tetravex.size; x_i++) printf("%d ", piece.bool_x[x_i]);
    printf("\n bool_y : ");
    for(int y_i = 0; y_i < tetravex.size; y_i++) printf("%d ", piece.bool_y[y_i]);
    printf("\n  /%d\\ \n", piece.number_up);
    printf("  %d %d \n", piece.number_left, piece.number_right);
    printf("  \\%d/ \n\n", piece.number_down);
}

//* Reads a given file to init a grid with squares inside
grid read_grid(string filename) {
    //> Get the file pointer
    FILE * file_pointer;
    file_pointer = fopen(filename, "r");

    //> Check if the file was open in "read" mode
    if (!file_pointer) FATAL_ERROR("read_grid - File was not found.", 1);
    
    int code;

    //> Get the size of the grid
    int size;
    code = fscanf(file_pointer, "%d", &size); 
    if (code != 1) FATAL_ERROR("read_grid - Size format issue in given file.", 1);
    grid new_grid = init_grid(size);

    //> Create every square of the grid 
    for(int square_i = 0; square_i < (new_grid.size * new_grid.size); square_i++) {
        
        //> Fill up numbers around the square
        int up, right, down, left;
        code = fscanf(file_pointer, "%d", &up); 
        if (code != 1) FATAL_ERROR("read_grid - Top number format issue in given file.", 1);
        code = fscanf(file_pointer, "%d", &right); 
        if (code != 1) FATAL_ERROR("read_grid - Right number format issue in given file.", 1);
        code = fscanf(file_pointer, "%d", &down); 
        if (code != 1) FATAL_ERROR("read_grid - Down number format issue in given file.", 1);
        if (feof(file_pointer)) FATAL_ERROR("read_grid - Not enough number in given file.", 2);
        code = fscanf(file_pointer, "%d\n", &left); 
        if (code != 1) FATAL_ERROR("read_grid - Left number format issue in given file.", 1);

        //> Create new square
        square new_square = init_square(new_grid, up, right, down, left);

        //> Add the square to the grid
        new_grid.tab[square_i] = new_square;
    }

    //> Filling up boolean literal for every coordinate of every square
    expression literal = 1;
    for (int square_i = 0; square_i < (new_grid.size * new_grid.size); square_i++) {
        for (int bool_i = 0; bool_i < new_grid.size; bool_i++) {
            new_grid.tab[square_i].bool_x[bool_i] = literal;
            literal++;
            new_grid.tab[square_i].bool_y[bool_i] = literal;
            literal++;
        }
    }

    return new_grid;
}