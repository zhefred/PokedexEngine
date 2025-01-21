import os
import sqlite3
from sqlite3 import Error


create_pokemons_table = """
CREATE TABLE IF NOT EXISTS pokedex(
    gen INTEGER NOT NULL,
    pokedex_nbr INTEGER PRIMARY KEY,
    price INTEGER,
    name TEXT NOT NULL,
    type TEXT[],
    height DOUBLE NOT NULL,
    weight DOUBLE,
    abilities TEXT[],
    gender_rate DOUBLE[],
    catch_rate INTEGER NOT NULL,
    leveling_rate TEXT NOT NULL,
    base_friendship INTEGER NOT NULL,
    base_exp_yield INTEGER NOT NULL,
    ev_yield INTEGER[],
    stats INTEGER[]    
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

create_effectiveness_table = """
    CREATE TABLE IF NOT EXISTS effectiveness(
        attacking_type TEXT PRIMARY KEY,
        normal DOUBLE NOT NULL,
        fire DOUBLE NOT NULL,
        water DOUBLE NOT NULL,
        electric DOUBLE NOT NULL,
        grass DOUBLE NOT NULL,
        ice DOUBLE NOT NULL,
        fighting DOUBLE NOT NULL,
        poison DOUBLE NOT NULL,
        ground DOUBLE NOT NULL,
        flying DOUBLE NOT NULL,
        psychic DOUBLE NOT NULL,
        bug DOUBLE NOT NULL,
        rock DOUBLE NOT NULL,
        ghost DOUBLE NOT NULL,
        dragon DOUBLE NOT NULL,
        dark DOUBLE NOT NULL,
        steel DOUBLE NOT NULL,
        fairy DOUBLE NOT NULL
        );
    """
path_parsed_file = "./pokedata/parsed_name_file.txt"
path_saved_file = "./pokedata/saved_name_file.txt"
path_raw_file = "./pokedata/raw_name_file.txt"
path_db = r"C:\Users\frede\Documents\Pi-kémon\website\pokeDb.sqlite"

def fill_pokemon_list():
    path = path_parsed_file.replace("name", "pokemons")
    if os.path.exists(path):
        f = open(path, "r")
        query = f.read()
        f.close()
        return str(query)
    else:
        raw_path = path_raw_file.replace("name", "pokemons")
        if os.path.exists(raw_path):
            print("raw file exists!")
        else:
            print("no such file exist, please create at least a file in raw data")            
            return None

def fill_move_list():
    path = path_parsed_file.replace("name", "move")
    if os.path.exists(path):
        f = open(path, "r")
        query = f.read()
        f.close()
        return str(query)
    else:
        raw_path = path_raw_file.replace("name", "move")
        if os.path.exists(raw_path):
            print("raw file exists!")
        else:
            print("no such file exist, please create at least a file in raw data")            
            return None
        
def fill_pokedex_list():
    path = path_saved_file.replace("name", "pokedex")
    if os.path.exists(path):
        f = open(path, "r")
        query = f.read()
        f.close()
        return str(query)
    else:
        print("no such file exist, please create at least a file in raw data")            
        return None
    
def fill_team_list():
    path = path_saved_file.replace("name", "team")
    if os.path.exists(path):
        f = open(path, "r")
        query = f.read()
        f.close()
        return str(query)
    else:
        print("no such file exist, please create at least a file in raw data")            
        return None
    
def fill_effectiveness_list():
    path = path_parsed_file.replace("name", "effectiveness")
    if os.path.exists(path):
        f = open(path, "r")
        query = f.read()
        f.close()
        return str(query)
    else:
        raw_path = path_raw_file.replace("name", "effectiveness")
        if os.path.exists(raw_path):
            print("raw file exists!")
        else:
            print("no such file exist, please create at least a file in raw data")            
            return None
        
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
        return connection
    except Error as e:
        print(f"The error '{e}' occured")
        return None

def execute_query(connection, query, success_message="", params=()):
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        connection.commit()
        if success_message :
            print(success_message)
    except Error as e:
        print(f"The error '{e}' occured")

def create_query(connection):
    ans = input("\n========CREATE========\n1 -> Create table Pokémon\n2 -> Create table Move\n3 -> Create table Team\n4 -> Create table Pokédex\n5 -> Create table effectiveness\n6 -> Create all tables\n0 -> Go back\n\n")

    if(ans == "1"):
        return create_pokemons_table
    elif(ans == "2"):
        return create_move_table
    elif(ans == "3"):
        return create_team_table
    elif(ans == "4"):
        return create_pokedex_table
    elif(ans == "5"):
        return create_effectiveness_table
    elif(ans =="6"):
        execute_query(connection, create_pokemons_table)
        execute_query(connection, create_move_table)
        execute_query(connection, create_team_table)
        execute_query(connection, create_pokedex_table)
        execute_query(connection, create_effectiveness_table)
        print("Done!")
        return ""
    elif(ans == "0"):
        return ""
    
def insert_query():
    ans = input("\n========INSERT========\n1 -> Insert into table Pokémon\n2 -> Insert into table Move\n3 -> Insert into table Team\n4 -> Insert into table Pokédex\n5 -> Insert into table effectiveness\n0 -> Go back\n\n")

    if(ans == "1"):
        res = fill_pokemon_list()
        if(res is not None):
            return res
        else :
            return ""
    elif(ans == "2"):
        res = fill_move_list()
        if(res is not None):
            return res
        else :
            return ""
    elif(ans == "3"):
        res = fill_team_list()
        if(res is not None):
            return res
        else :
            return ""
    elif(ans == "4"):
        res = fill_pokedex_list()
        if(res is not None):
            return res
        else :
            return ""
    elif(ans == "5"):
        res = fill_effectiveness_list()
        if(res is not None):
            return res
        else :
            return ""


def update_query():
    return ""
    
def delete_query(connection):
    ans = input("\n========DELETE========\n1 -> Delete table Pokémon\n2 -> Delete table Move\n3 -> Delete table Team\n4 -> Delete table Pokédex\n5 -> Delete table effectiveness\n0 -> Go back\n\n")

    query = "DROP TABLE ";

    if(ans == "1"):
        query += ("pokemon;")
    elif (ans == "2"):
        query.append("move;")
    elif (ans == "3"):
        query.append("team;")
    elif (ans == "4"):
        query.append("pokedex;")
    elif (ans == "5"):
        query.append("effectiveness;")
    else :
        return 

def main():
    connection = create_connection(path_db)
    prompt = "\nWhat do you want to do?\n\n1 -> Create\n2 -> Insert data\n3 -> Update\n4 -> Delete\n0 -> Quit\n\n"

    ans = input(prompt)

    query_to_execute = ""

    while(ans != "0"):
        if(ans == "1"):
            query_to_execute = create_query(connection)
        elif(ans == "2"):
            query_to_execute = insert_query()
        elif(ans == "3"):
            query_to_execute = update_query()
        elif(ans == "4"):
            query_to_execute = delete_query(connection)

        if(query_to_execute != ""):
            execute_query(connection, query_to_execute)
            print("Done!")
        
        ans = input(prompt)

if __name__ == "__main__":
    main()