import requests

def get_help():

    print("------ POMOC ------")
    print(f"1: Podaj nazwy wszystkich pokemonów (alfabetycznie")


    userinput = input("Co potrzebujesz: (podaj numer 1-6) (wpisz: 9, aby wyjść)")

    while True:
        if userinput == "9":
            break


def get_all_pokemon():

    r = requests.get("https://pokeapi.co/api/v2/pokemon?limit=150")

    response = r.json()
    # print(response["results"])
    pokemon_list = sorted([pokemon["name"] for pokemon in response["results"]])
    print(pokemon_list[0])
    print("------ Lista Pokemonów ------")
    ent = 0
    for pokemon in pokemon_list:
        print(pokemon, end=', ')
        if ent == 7:
            print("")
            ent = 0
        ent = ent + 1
    print("\n-----------------------")


print(get_all_pokemon())