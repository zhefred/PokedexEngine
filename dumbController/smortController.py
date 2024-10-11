"""
- Permettre au code de sélectionner ses Pokémons
- Permettre au code de sélectionner le move
- Permettre au code de sélectionner sa récompense
- Guider le code pour éviter qu'il aie à lire à l'écran (pour le moment)
"""
import db_handler

"""|OFFo oON                  |
   | .----------------------. |
   | |  .----------------.  | |
   | |  |                |  | |
   | |))|                |  | |
   | |  |                |  | |
   | |  |                |  | |
   | |  |                |  | |
   | |  |                |  | |
   | |  |                |  | |
   | |  '----------------'  | |
   | |__GAME BOY____________/ |
   |          ________        |
   |    __   (Nintendo)       |
   |  _|W|_   """"""""   .-.  |
   | [A   D]        .-. ( Z ) |
   |  | S|         ( X ) '-'  |
   |                '-'   A   |
   |                 B        |
   |          ___   _____     |
   |         (_M_) (Enter),., |
   |        select start ;:;: |
   |                    ,;:;' /
   |                   ,:;:'.'
   '-----------------------`
"""

def main():
    #Start the db
    db_handler.initialize_database()
    #New Game
    print("please start a new game")

    #select random pokemons for the starter team
    starting_amount = 10
    db_handler.create_starting_team(10)
if __name__ == "__main__":
    main()