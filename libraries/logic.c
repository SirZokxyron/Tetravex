#include "../includes/logic.h"

//* Return the string combination representing the CNJ form of the "header" for the file
void header(grid tetravex, FILE * filepointer) {
    return;
}

//* Return the string combination representing the CNJ form of "coordinate unicity" for each square
void coord_unicity(grid tetravex, FILE * filepointer) {
    for(int square_i = 0; square_i < (tetravex.size * tetravex.size); square_i++) {
        
        string unicity_x = "";
        string unicity_neg_x = "";
        string unicity_y = "";
        string unicity_neg_y = "";
        
        for(int bool_i = 0; bool_i < tetravex.size; bool_i++) {
            unicity_x = concat_exp(unicity_x, tetravex.tab[square_i].bool_x[bool_i]); 
            unicity_neg_x = concat_exp(unicity_neg_x, neg(tetravex.tab[square_i].bool_x[bool_i]));
            unicity_y = concat_exp(unicity_y, tetravex.tab[square_i].bool_y[bool_i]);
            unicity_neg_y = concat_exp(unicity_neg_y, neg(tetravex.tab[square_i].bool_y[bool_i]));
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

//* Return the string combination representing the CNJ form of "non superposition" for each square combo
void non_superposition(grid tetravex, FILE * filepointer) {
    for(int square_1_i = 0; square_1_i < (tetravex.size * tetravex.size); square_1_i++) {
        for(int square_2_i = square_1_i + 1; square_2_i < (tetravex.size * tetravex.size); square_2_i++) {
            for(int coord_1_i = 0; coord_1_i < tetravex.size; coord_1_i++) {
                string test_1 = "";
                string test_2 = "";
                string test_3 = "";
                string test_4 = "";
                test_1 = concat_exp(test_1, neg(tetravex.tab[square_1_i].bool_x[coord_1_i]));
                test_2 = concat_exp(test_2, neg(tetravex.tab[square_1_i].bool_x[coord_1_i]));
                test_3 = concat_exp(test_3, neg(tetravex.tab[square_1_i].bool_y[coord_1_i]));
                test_4 = concat_exp(test_4, neg(tetravex.tab[square_1_i].bool_y[coord_1_i]));
                test_1 = concat_exp(test_1, neg(tetravex.tab[square_2_i].bool_x[coord_1_i]));
                test_2 = concat_exp(test_2, neg(tetravex.tab[square_2_i].bool_x[coord_1_i]));
                test_3 = concat_exp(test_3, neg(tetravex.tab[square_2_i].bool_y[coord_1_i]));
                test_4 = concat_exp(test_4, neg(tetravex.tab[square_2_i].bool_y[coord_1_i]));
                for(int coord_2_i = 0; coord_2_i < tetravex.size; coord_2_i++) {
                    if (!coord_2_i) {
                        test_1 = concat_exp(test_1, tetravex.tab[square_1_i].bool_y[coord_2_i]);
                        test_3 = concat_exp(test_3, tetravex.tab[square_1_i].bool_x[coord_2_i]);
                        test_1 = concat_exp(test_1, tetravex.tab[square_2_i].bool_y[coord_2_i]);
                        test_3 = concat_exp(test_3, tetravex.tab[square_2_i].bool_x[coord_2_i]);
                    } else {
                        test_2 = concat_exp(test_2, tetravex.tab[square_1_i].bool_y[coord_2_i]);
                        test_4 = concat_exp(test_4, tetravex.tab[square_1_i].bool_x[coord_2_i]);
                        test_2 = concat_exp(test_2, tetravex.tab[square_2_i].bool_y[coord_2_i]);
                        test_4 = concat_exp(test_4, tetravex.tab[square_2_i].bool_x[coord_2_i]);
                    }
                }
                test_1 = concat_exp(test_1, 0);
                test_2 = concat_exp(test_2, 0);
                test_3 = concat_exp(test_3, 0);
                test_4 = concat_exp(test_4, 0);
                fprintf(filepointer, "%s", test_1);
                fprintf(filepointer, "%s", test_2);
                fprintf(filepointer, "%s", test_3);
                fprintf(filepointer, "%s", test_4);
            }
        }
    }
}

//* Return the string combination representing the CNJ form of "number logic" for each square
void number_logif(grid tetravex, FILE * filepointer) {
    return;
}