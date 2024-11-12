"""
- Permettre au code de sélectionner ses Pokémons
- Permettre au code de sélectionner le move
- Permettre au code de sélectionner sa récompense
- Guider le code pour éviter qu'il aie à lire à l'écran (pour le moment)
"""
import db_handler
import take_control

def main():
    #Start the db
    db_handler.initialize_database()
    #Start the controller
    #controller = take_control.plug_controller()
    #New Game
    take_control.start_new_game()

    #select random pokemons for the starter team
    starting_amount = 10

    db_handler.create_starting_team(starting_amount)

if __name__ == "__main__":
    main()