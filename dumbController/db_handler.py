import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occured")
    
    return connection

connection = create_connection("./dumbController/pokeDb.sqlite")

def execute_query(connection, query, success_message):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        if(success_message != ""):
            print(success_message)
    
    except Error as e:
        print(f"The error '{e}' occured")

def get_query():
    f = open("./dumbController/sql_query_file.txt", "r")
    query = f.read()
    f.close()
    return str(query)

def new_pokedex_entry(pokemon):
    is_on_the_list = f"SELECT COUNT(*) FROM pokemon WHERE pokedex_nbr = 1"
    if(is_on_the_list):
        add_pokemon = f"INSERT INTO pokedex SELECT * FROM pokemon where pokedex_nbr = 1"
        
        find_pokemon = f"SELECT * FROM pokemon where pokedex_nbr = 1"
        pokemon_added = execute_query(connection, find_pokemon, "")

        execute_query(connection, add_pokemon, pokemon_added)
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
        ability TEXT NOT NULL,
        iv INTEGER[] NOT NULL
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

    starters = [1, 4]
    #, 7, 152, 155, 158, 252, 255, 258, 387, 390, 393, 495, 498, 501, 650, 653, 656, 722, 725, 728, 810, 813, 816, 906, 909, 912]

    for pokemon in starters:
        new_pokedex_entry(pokemon)

def get_pokemon_info(pokedex_nbr):
    fetch_infos = f"SELECT * FROM pokedex WHERE pokedex_nbr = {pokedex_nbr}"
    rep = execute_query(connection, fetch_infos,"")

    
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