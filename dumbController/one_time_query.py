import os
import sqlite3
from sqlite3 import Error


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

def fill_pokemon_list():
    path = "./pokedata/parsed_pokemons_file.txt"
    if os.path.exists(path):
        f = open(path, "r")
        query = f.read()
        f.close()
        return str(query)
    else:
        return None

def fill_move_list():
    f = open("./pokedata/parsed_move_file.txt", "r")
    query = f.read()
    f.close()
    return str(query)

def fill_pokedex_list():
    path = "./pokedata/saved_pokedex_file.txt"
    if os.path.exists(path):
        f = open(path, "r")
        query = f.read()
        f.close()
        return str(query)
    else:
        return None

def fill_team_list():
    path = "./pokedata/saved_team_file"
    if os.path.exists(path):
        f = open(path, "r")
        query = f.read()
        f.close()
        return str(query)
    else:
        return None

def fill_effectiveness_list():
    f = open("./pokedata/parsed_effectiveness_file.txt", "r")
    query = f.read()
    f.close()
    return query

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

def create_query():
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
        return fill_pokemon_list()
    elif(ans == "2"):
        return fill_move_list()
    elif(ans == "3"):
        res = fill_team_list()
        if(res is not None):
            return res
        else :
            print("File does not exist")
            return ""
    elif(ans == "4"):
        res = fill_pokedex_list()
        if(res is not None):
            return res
        else :
            print("File does not exist")
            return ""


def update_query():
    return ""
    
def delete_query():
    return ""

def main():
    prompt = "\nWhat do you want to do?\n\n1 -> Create\n2 -> Insert data\n3 -> Update\n4 -> Delete\n0 -> Quit\n\n"

    ans = input(prompt)

    query_to_execute = ""

    while(ans != "0"):
        if(ans == "1"):
            query_to_execute = create_query()
        elif(ans == "2"):
            query_to_execute = insert_query()
        elif(ans == "3"):
            query_to_execute = update_query()
        elif(ans == "4"):
            query_to_execute = delete_query()

        if(query_to_execute != ""):
            execute_query(connection, query_to_execute)
            print("Done!")
        
        ans = input(prompt)

if __name__ == "__main__":
    main()