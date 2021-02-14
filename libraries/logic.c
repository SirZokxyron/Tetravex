#include "../includes/logic.h"

//* Return the string combination representing the CNJ form of coordinate unicity for each square
void coord_unicity(grid tetravex, FILE * filepointer) {

    for(int square_i = 0; square_i < (tetravex.size * tetravex.size); square_i++) {
        for(int bool_x_i = 0; bool_x_i < tetravex.size; bool_x_i++) {
            fprintf(filepointer, "%d ", tetravex.tab[square_i].bool_x[bool_x_i]);
        }
        fprintf(filepointer, "0\n");
        for(int bool_y_i = 0; bool_y_i < tetravex.size; bool_y_i++) {
            fprintf(filepointer, "%d ", tetravex.tab[square_i].bool_y[bool_y_i]);
        }
        fprintf(filepointer, "0\n");
        for(int bool_x_i = 0; bool_x_i < tetravex.size; bool_x_i++) {
            fprintf(filepointer, "%d ", neg(tetravex.tab[square_i].bool_x[bool_x_i]));
        }
        fprintf(filepointer, "0\n");
        for(int bool_y_i = 0; bool_y_i < tetravex.size; bool_y_i++) {
            fprintf(filepointer, "%d ", neg(tetravex.tab[square_i].bool_y[bool_y_i]));
        }
        fprintf(filepointer, "0\n");
    }
}