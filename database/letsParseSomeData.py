def pokemon_data_parser(raw_path):
    f = open(raw_path, "r")
    raw = f.read()
    f.close()
    #gets raw_pokemons_file.txt

    raw_pokeDb = raw.split("\n") #Separates every line

    pokeDb = [[0] for i in range(len(raw_pokeDb))] #stores every line in a cell in an array

    for pokemon in range(0, len(raw_pokeDb)):
        pokeDb[pokemon] = raw_pokeDb[pokemon].split("\t") #Separates every info on the line

    sqlite_query = open((raw_path.replace("raw", "parsed")), "w") #opens parsed_pokemons_file.txt or creates it if it doesn't exist yet

    sqlite_query.write("INSERT INTO\n   pokedex (gen, pokedex_nbr, price, name, type, height, weight, abilities, gender_rate, catch_rate, leveling_rate, base_friendship, base_exp_yield, ev_yield, stats)\nVALUES\n")
    #writes the initial sql query

    for x in range(len(pokeDb)): #x is the pokemon line, y is the infos of that specific pokemon
        pokemon_infos = "   ("
        for y in range(len(pokeDb[x])):
            #gen, pokedex_nbr, price, name, {type1, type2}, height, weight, {ability1, ability2, hidden_ability}, {male_rate, female_rate}, catch_rate, leveling_rate, bf, bey, {HP_yield, ATK_yield, DEF_yield, SPATK_yield, SPDEF_yield, SPD_yield}, {HP, ATK, DEF, SPATK, SPDEF, SPD}
            if(y in (4, 8, 11, 17, 23)):
                pokemon_infos += "'{"
                pokemon_infos += "\"{}\"".format(pokeDb[x][y])
            elif(y in (5, 10, 12, 22, 28)):
                pokemon_infos += "\"{}\"".format(pokeDb[x][y])
                pokemon_infos += "}'"
            else:
                pokemon_infos += "\"{}\"".format(pokeDb[x][y])

            if(y < 28):
                pokemon_infos += ", "
        if(x < len(pokeDb)-1):
            pokemon_infos += "),\n"
        else:
            pokemon_infos += "\n);\n"
        sqlite_query.write(pokemon_infos)

    print("Done!")

def effectiveness_data_parser(raw_path):
    f = open(raw_path, "r")
    raw = f.read()
    f.close()

    raw_effectiveness_file = raw.split("\n")

    eff_table = [[0] for i in range(len(raw_effectiveness_file))]

    for eff in range(0, len(eff_table)):
        effectiveness = raw_effectiveness_file[eff].split("|\t")
        for type_eff in range(0, len(effectiveness)):
            if "->" in effectiveness[type_eff]:
                effectiveness[type_eff] = effectiveness[type_eff][:-3].strip()
            elif effectiveness[type_eff] == 'Â½':
                effectiveness[type_eff] = float("0.5")
            else :
                effectiveness[type_eff] = float(effectiveness[type_eff])

        eff_table[eff] = effectiveness

    sqlite_query = open((raw_path.replace("raw", "parsed")), "w")

    sqlite_query.write("")

    sqlite_query.write("INSERT INTO\n   effectiveness (normal)")
    print("Done!")

def main():
    pokemon_data_parser("./pokedata/raw_pokemons_file.txt")

if __name__ == "__main__":
    main()