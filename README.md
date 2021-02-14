    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #       ////////   //    //   ////////   //    //   ////////   ////////   #
    #         //      ///   //   //         //    //   //    //         //    #
    #        //      // // //   ////////   ////////   //    //   ////////     #
    #       //      //   ///   //               //   //    //   //            #
    #   ////////   //    //   //               //   ////////   ////////       #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

Authors : _Bensbia Hugo ; Rousselle Naomi ; Tellier Rozen Adjamé ; Romain Noé_

# Brief description

This repository contains our project at solving a game of Tetravex using Boolean logic with a SAT-Solver. It's part of our INF402 course at the Grenoble-Alpes-University.

# How we are doing it

In the first place, we need to describe the rule of a Tetravex using boolean logic. We'll determine the conditions of every **piece** of a **valid** grid of Tetravex. 

Then we'll use an algorithm to combine these **static parameters** with our **instance** of the game to output a DIMACS file. 

Finally, using a SAT-Solver and the DIMACS file we'll be able to test the satisfiability of the instance of the game, which would indicate if it is possible to solve the grid and how to.
 
# Which SAT-Solver 

- **TO-DO :** Find which SAT-Solver to use. And how to extract the results to determine the solution of the game.

# Repository description

## blueprints

This directory is made of two sub-directories
- `tetra`   : contains every `.tetra` file used to create instances of a game.
- `dimacs`  : contains every `.cnf` file used to describe the game using boolean logic.

## libraries

This directory contains our `.c` packages.

## includes

This directory contains our `.h` interfaces for every package in the libraries folder.

## tests

This directory contains all our executables source codes. They are used to verify the validity of our packages and algorithms.

## Makefile

This file is used to compile our project.
Available commands :

- `make`        : Compile all executables
- `make clean`  : Delete every `.o` file
- `make clear`  : Delete all executables

## README

You are currently reading this file.
