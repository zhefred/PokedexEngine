"""
- Permettre au code de sélectionner ses Pokémons
- Permettre au code de sélectionner le move
- Permettre au code de sélectionner sa récompense
- Guider le code pour éviter qu'il aie à lire à l'écran (pour le moment)
"""
import db_handler
import random

#Start the db
db_handler.initialize_database()

#Set up the commands


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
#New Game
print("please start a new game")

#select random pokemons
#db_handler.get_pokemon_info(1)