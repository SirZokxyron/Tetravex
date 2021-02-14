#ifndef _TETRAVEX_H_
#define _TETRAVEX_H_

#include "../includes/boolean.h"

/* Data structures */

    //* Square structure, representing a square of Tetravex
    typedef struct square_ {
        //> The array with every boolean associated with a specific x position
        expression * bool_x;
        //> The array with every boolean associated with a specific y position
        expression * bool_y;        
        //> Every number around the square
        int number_up;
        int number_right;
        int number_down;
        int number_left;
    } square;

    //* Grid structure, representing a grid of Tetravex
    typedef struct grid_ {
        int size;           //> Size of the side, since it's a square it's (size * size)
        square * tab;       //> The array with every square inside
    } grid;

/* Functions */

    //* Returns a grid with the correct given size and allocates the memory for the square array
    grid init_grid(int size);

    //* Returns a square with the correct given numbers around it and allocates the memory for every coordinate boolean array
    square init_square(grid tetravex, int number_up, int number_right, int number_down, int number_left);

    //? Debug function to print out square parameters
    void debug_square(grid tetravex, square piece, int name);

    //* Reads a given file to init a grid with squares inside
    grid read_grid(string filename);

#endif