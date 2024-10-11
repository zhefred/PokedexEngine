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

connection = create_connection("./dumbController/pokeDb.sqlite")

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
    cursor = connection.cursor()
    try :
        cursor.execute(query, params)
        rep = cursor.fetchone()
        if rep is not None :
            return rep[index_to_fetch]
        else :
            return None
    except Error as e :
        print(f"Error '{e}' has occured")
        return None

def fetch_all(query, params=()):
    cursor = connection.cursor()
    try :
        cursor.execute(query, params)
        rep = cursor.fetchall()
        return [row[0] for row in rep]
    except Error as e :
        print(f"Error '{e}' has occured")
        return None
    
def create_starting_team(starting_amount):
    print("")
    current_amount = starting_amount

    while check_if_can_buy(current_amount):
        #get your current team
        current_team = fetch_all("SELECT pokedex_nbr FROM team")

        if current_team:
            current_team = [pokemon[0] for pokemon in current_team]
        else :
            current_team = []

        query = "SELECT pokedex_nbr, price, name FROM pokedex WHERE pokedex_nbr NOT IN ({})".format(
            ','.join('?' * len(current_team))
        )
        #see the pokemons still available
        available_pokemon = fetch_all(query, current_team)

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
    
def get_query():
    f = open("./dumbController/sql_query_file.txt", "r")
    query = f.read()
    f.close()
    return str(query)

def new_pokedex_entry(pokemon):
    # is_on_the_list = fetch_one(f"SELECT COUNT(*) FROM pokemon WHERE pokedex_nbr IS {pokemon}",0)
    if(pokemon > 0 and pokemon < 1025):
        add_pokemon = f"INSERT INTO pokedex SELECT * FROM pokemon where pokedex_nbr IS {pokemon}"
        
        find_pokemon = f"SELECT * FROM pokemon where pokedex_nbr = {pokemon}"
        pokemon_added = fetch_one(find_pokemon,2)

        execute_query(connection, add_pokemon, f"{pokemon_added} has been added to your pokedex")
    else:
        print("The pokemon you're trying to add doesn't exist!")


def initialize_database():
    create_pokemons_table = """
    CREATE TABLE IF NOT EXISTS pokemon(
        pokedex_nbr INTEGER PRIMARY KEY,
        price INTEGER,
        name TEXT NOT NULL,
        type1 TEXT NOT NULL,
        type2 TEXT,
        height DOUBLE NOT NULL,
        weight DOUBLE,
        ability1 TEXT NOT NULL,
        ability2 TEXT,
        hidden_ability TEXT
    );
    """
    #The number of evos include the stage we are at

    create_move_table = """
    CREATE TABLE IF NOT EXISTS move(
        name TEXT PRIMARY KEY,
        type TEXT NOT NULL,
        category TEXT,
        power INTEGER,
        accuracy INTEGER,
        pp INTEGER NOT NULL,
        makesContact BOOLEAN NOT NULL,
        priority INTEGER NOT NULL,
        effect TEXT NOT NULL,
        target TEXT NOT NULL
    );
    """

    create_team_table = """
    CREATE TABLE IF NOT EXISTS team(
        pokedex_nbr INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        type1 TEXT NOT NULL,
        type2 TEXT,
        ability TEXT NOT NULL
    );
    """

    create_pokedex_table = """
    CREATE TABLE IF NOT EXISTS pokedex(
        pokedex_nbr INTEGER PRIMARY KEY,
        price INTEGER,
        name TEXT NOT NULL,
        type1 TEXT NOT NULL,
        type2 TEXT,
        height DOUBLE NOT NULL,
        weight DOUBLE,
        ability1 TEXT NOT NULL,
        ability2 TEXT,
        hidden_ability TEXT
    );"""

    execute_query(connection, create_pokemons_table, "Succesfully created table Pokemon")
    execute_query(connection, create_move_table, "Succesfully created table Move")
    execute_query(connection, create_team_table, "Succesfully created table Team")
    execute_query(connection, create_pokedex_table, "Succesfully created table Pokedex")

    
    
    table__is_empty = execute_query(connection, "select count(*) FROM pokemon limit 1", "") == 0

    if(not table__is_empty):
        delete_pokemons = """DELETE FROM pokemon"""
        reset_counter_pokemons = """DELETE FROM SQLITE_SEQUENCE WHERE name='pokemon'"""
        execute_query(connection, delete_pokemons,"")
        execute_query(connection, reset_counter_pokemons,"")

        erase_pokedex = "DELETE FROM pokedex"
        reset_counter_pokedex = "DELETE FROM SQLITE_SEQUENCE WHERE name='pokedex'"
        execute_query(connection, erase_pokedex, "")
        execute_query(connection, reset_counter_pokedex, "")
        
    list_pokemon = get_query()

    execute_query(connection, list_pokemon, "Pokemon have been listed in the database")

    starters = [1, 4, 7, 152, 155, 158, 251, 254, 257, 387, 389, 393, 495, 498, 501, 650, 653, 656, 722, 725, 728, 810, 813, 816, 906, 909, 912]

    for pokemon in starters:
        new_pokedex_entry(pokemon)

def get_pokemon_info(pokedex_nbr):
    fetch_infos = f"SELECT * FROM pokedex WHERE pokedex_nbr = {pokedex_nbr}"
    cursor = connection.cursor()

    try :
        cursor.execute(fetch_infos)
        rep = cursor.fetchall()
        return rep[0]
    except Error as e :
        print(f"Error '{e}' has occured")
        return None

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