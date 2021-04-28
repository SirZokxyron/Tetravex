    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #       ////////   //    //   ////////   //    //   ////////   ////////   #
    #         //      ///   //   //         //    //   //    //         //    #
    #        //      // // //   ////////   ////////   //    //   ////////     #
    #       //      //   ///   //               //   //    //   //            #
    #   ////////   //    //   //               //   ////////   ////////       #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

Auteurs : _Bensbia Hugo ; Rousselle Naomi ; Tellier Rozen Adjamé ; Romain Noé_

# Utilisation du programme

- Lancer le programme main.py avec python 3.7 ou supérieur.
- *OPTIONNEL* ouvrir les logs
- Charger une grille d'un fichier ou en la générant en indiquant la taille d'un coté.
- Appliquer une ou plusieurs règles de logique.
- Creer le fichier .cnf
- Creer le fichier .output
- Observer si la grille est resolvable

# Bref description

Ce dossier contient notre projet qui consiste à résoudre une partie de Tetravex en utilisant la logique propositionnelle et un SAT-Solver. Ce projet fait parti de notre cours d'INF402 à l'Université-Grenoble-Alpes.

# Comment on procède

Tout d'abord, nous devons décrire les règles d'une partie classique en utilisant la logique propositionnelle. Nous déterminons les conditions de toutes les **pièces** d'une grille de Tetravex **valide**.

Ensuite, nous utilisons un algorithme pour combiner ces **paramètres statiques** avec notre **instance** du jeu pour créer un fichier DIMACS.

Finallement, nous utilisons un SAT-Solver pour traiter le fichier DIMACS généré et test la satisfaisabilité de notre instance, ce qui nous indique si on peut résoudre la grille et **comment**.
 
# Quel SAT-Solver

- **SAT4j :** Nous utilisons SAT4J pour traiter nos fichier DIMACS.

# Description du dossier

## Samples

Ce dossier contient nos fichier .tetra qui définissent des instances d'une partie de Tetravex.

## dimacs

Ce dossier contient les fichiers crées par le traitement des instances de Tetravex

## README

You are currently reading this file.
