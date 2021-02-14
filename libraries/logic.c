#include "../includes/logic.h"

//* Return the string combination representing the CNJ form of coordinate unicity for each square
void coord_unicity(grid tetravex, FILE * filepointer) {
    for(int square_i = 0; square_i < (tetravex.size * tetravex.size); square_i++) {
        
        string unicity_x = "";
        string unicity_neg_x = "";
        string unicity_y = "";
        string unicity_neg_y = "";
        
        for(int bool_x_i = 0; bool_x_i < tetravex.size; bool_x_i++) {
            unicity_x = concat_exp(unicity_x, tetravex.tab[square_i].bool_x[bool_x_i]); 
            unicity_neg_x = concat_exp(unicity_neg_x, neg(tetravex.tab[square_i].bool_x[bool_x_i]));
        }
        for(int bool_y_i = 0; bool_y_i < tetravex.size; bool_y_i++) {
            unicity_y = concat_exp(unicity_y, tetravex.tab[square_i].bool_y[bool_y_i]);
            unicity_neg_y = concat_exp(unicity_neg_y, neg(tetravex.tab[square_i].bool_y[bool_y_i]));
        }

        unicity_x = concat_exp(unicity_x, 0);
        unicity_neg_x = concat_exp(unicity_neg_x, 0);
        unicity_y = concat_exp(unicity_y, 0);
        unicity_neg_y = concat_exp(unicity_neg_y, 0);
        fprintf(filepointer, "%s", unicity_x);
        fprintf(filepointer, "%s", unicity_neg_x);
        fprintf(filepointer, "%s", unicity_y);
        fprintf(filepointer, "%s", unicity_neg_y);
    }
}