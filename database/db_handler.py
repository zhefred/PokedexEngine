import sqlite3
from sqlite3 import Error
import random

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occured")
    
    return connection

def execute_query(connection, query, success_message="", params=()):
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        connection.commit()
        if success_message :
            print(success_message)
    except Error as e:
        print(f"The error '{e}' occured")

def fetch_one(query, index_to_fetch, params=()):
    connection = create_connection("./dumbController/pokeDb.sqlite")
    cursor = connection.cursor()
    try :
        cursor.execute(query, params)
        rep = cursor.fetchone()
        connection.close()
        if rep is not None :            
            return rep[index_to_fetch]
        else :
            return None
    except Error as e :
        print(f"Error '{e}' has occured")
        return None

def fetch_all(query, params=()):
    connection = create_connection("./dumbController/pokeDb.sqlite")
    cursor = connection.cursor()
    try :
        cursor.execute(query, params)
        rep = cursor.fetchall()
        connection.close()
        return [row[0] for row in rep]
    except Error as e :
        print(f"Error '{e}' has occured")
        connection.close()
        return None
    
def create_starting_team(starting_amount):
    connection = create_connection("./dumbController/pokeDb.sqlite")

    current_amount = starting_amount

    while check_if_can_buy(current_amount):
        #get your current team
        current_team = fetch_all("SELECT pokedex_nbr FROM team")

        query = "SELECT pokedex_nbr, price, name FROM pokedex WHERE pokedex_nbr NOT IN ({})".format(
            ','.join('?' * len(current_team))
        )
        #see the pokemons still available
        pokemon_in_pokedex = fetch_all(query, current_team)
        available_pokemon = []
        for pokemon in pokemon_in_pokedex:
            poke_price = get_pokemon_info(pokemon)
            if (poke_price[1] <= current_amount):
                available_pokemon.append(pokemon)

        if not available_pokemon :
            print("No available Pokémon to add.")
            break
        
        #add a random one
        next_pokemon = available_pokemon[random.randint(0, len(available_pokemon) - 1)]
        pokemon_to_add = get_pokemon_info(next_pokemon)
        query = f"INSERT INTO team (pokedex_nbr, name, type1, type2, ability) SELECT pokedex_nbr, name, type1, type2, ability1 FROM pokedex WHERE pokedex_nbr = {pokemon_to_add[0]}"
        execute_query(connection, query)
        print(f"{pokemon_to_add[2]} has been added to your team!")

        current_amount -= pokemon_to_add[1]   
        connection.close()

def check_if_can_buy(current_amount):
    get_team = "SELECT pokedex_nbr FROM team"
    current_team = fetch_all(get_team)

    price_query = "SELECT price FROM pokedex WHERE pokedex_nbr NOT IN ({seq})".format(
        seq=','.join(['?']*len(current_team))
    )

    available_prices = fetch_all(price_query, current_team)
    for price in available_prices:
        if (price < current_amount):
            return True
    return False
    

def new_pokedex_entry(pokemon):
    connection = create_connection("./dumbController/pokeDb.sqlite")

    # is_on_the_list = fetch_one(f"SELECT COUNT(*) FROM pokemon WHERE pokedex_nbr IS {pokemon}",0)
    if(pokemon > 0 and pokemon < 1025):
        add_pokemon = f"INSERT INTO pokedex SELECT * FROM pokemon where pokedex_nbr IS {pokemon}"
        
        find_pokemon = f"SELECT * FROM pokemon where pokedex_nbr = {pokemon}"
        pokemon_added = fetch_one(find_pokemon,2)

        execute_query(connection, add_pokemon, f"{pokemon_added} has been added to your pokedex")
    else:
        print("The pokemon you're trying to add doesn't exist!")
    
    connection.close()


def initialize_database():
    connection = create_connection("./dumbController/pokeDb.sqlite")

    table__is_empty = execute_query(connection, "select count(*) FROM pokemon limit 1", "") == 0

    if(not table__is_empty):
        erase_team = "DELETE FROM team"
        reset_counter_team = "DELETE FROM SQLITE_SEQUENCE WHERE name='team'"
        execute_query(connection, erase_team, "")
        execute_query(connection, reset_counter_team, "")
        
    starters = [1, 4, 7, 152, 155, 158, 251, 254, 257, 387, 389, 393, 495, 498, 501, 650, 653, 656, 722, 725, 728, 810, 813, 816, 906, 909, 912]

    for pokemon in starters:
        new_pokedex_entry(pokemon)
    
    connection.close()

def get_pokemon_info(pokedex_nbr):
    connection = create_connection("./dumbController/pokeDb.sqlite")

    fetch_infos = f"SELECT * FROM pokedex WHERE pokedex_nbr = {pokedex_nbr}"
    cursor = connection.cursor()

    try :
        cursor.execute(fetch_infos)
        rep = cursor.fetchall()
        connection.close()
        return rep[0]
    except Error as e :
        print(f"Error '{e}' has occured")
        connection.close()
        return None
    
def get_size_of(table):
    query = f"SELECT COUNT(*) FROM {table}"
    size = fetch_one(query, 0)
    return size
    

def main():
    welcome = """
⠀⠀⠀⠀⠀⠀⠀⣾⣶⣄⡀⡄⣀⣀⣴⣶⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢨⣧⡶⣼⣴⣦⣮⢿⣿⣿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡁⠙⡿⠛⠉⠈⢿⣿⣿⣿⣧⠀⠀⠀⠀
⠀⠀⠀⠀⢄⣦⢐⠀⠀⠐⠂⠀⠀⣿⣿⣿⣿⢀⡀⠀⠀
⠀⠀⠀⠀⣿⣿⠈⠙⠛⠛⠉⣠⣰⣿⣿⣿⣿⣿⣿⣧⠀
⠀⠀⠀⠀⡻⠋⠀⠀⠀⠈⠀⠀⠸⣿⣿⣿⣿⣿⣿⡿⠀
⠀⠀⠀⢀⠁⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⡅⠀
⠀⠀⠀⡌⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⠀
⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣽⡆
⠠⣰⡀⢴⠀⠀⠀⠀⠀⠀⠀⣰⣰⣿⣿⣿⣿⣿⣿⣯⠇
⠀⢝⠒⣼⢳⣄⠀⡀⢀⣴⣾⣿⣿⡿⠋⠻⠩⢿⣿⠟⠀
⠀⠀⠢⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⢀⣀⠀⢹⠀⠀
⠀⠀⠀⠀⠉⠉⠁⠀⠉⠉⠙⠛⠛⠢⠴⠿⠿⠣⠁⠀⠀

 _    _      _                          
| |  | |    | |                         
| |  | | ___| | ___ ___  _ __ ___   ___ 
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \
\  /\  /  __/ | (_| (_) | | | | | |  __/
 \/  \/ \___|_|\___\___/|_| |_| |_|\___|
                                        
    """

if __name__ == "__main__":
    main()