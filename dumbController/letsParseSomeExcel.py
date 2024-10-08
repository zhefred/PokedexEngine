f = open("./dumbController/pokeDb.txt", "r")
raw = f.read()
f.close()

raw_pokeDb = raw.split("\n")

pokeDb = [[0] for i in range(len(raw_pokeDb))]

for pokemon in range(0, len(raw_pokeDb)):
    pokeDb[pokemon] = raw_pokeDb[pokemon].split("\t")

sqlite_query = open("./dumbController/sql_query_file.txt", "w")

sqlite_query.write("INSERT INTO\n   pokemon (pokedex_nbr, name, type1, type2, height, weight, ability1, ability2)\nVALUES\n")

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