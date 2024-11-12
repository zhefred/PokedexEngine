def pokemon_data_parser(raw_path):
    f = open(raw_path, "r")
    raw = f.read()
    f.close()

    raw_pokeDb = raw.split("\n")

    pokeDb = [[0] for i in range(len(raw_pokeDb))]

    for pokemon in range(0, len(raw_pokeDb)):
        pokeDb[pokemon] = raw_pokeDb[pokemon].split("\t")

    sqlite_query = open((raw_path.replace("raw", "parsed")), "w")

    sqlite_query.write("INSERT INTO\n   pokemon (pokedex_nbr, price, name, type1, type2, height, weight, ability1, ability2)\nVALUES\n")

    for x in range(len(pokeDb)):
        pokemon_infos = "   ("
        for y in range(8):
            pokemon_infos += "\"{}\"".format(pokeDb[x][y])
            if(y < 7):
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
    effectiveness_data_parser("./pokedata/raw_effectiveness_file.txt")

if __name__ == "__main__":
    main()