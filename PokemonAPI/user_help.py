import requests
from get_data import get_pokemon
def get_help():

    print("------ POMOC ------")
    print(f"1: Nazwy wszystkich pokemonów (alfabetycznie)")
    print("(podaj numer 1-6) (wpisz: 9, aby się cofnąć)")


    while True:
        userinput = input("Co potrzebujesz: ")
        if userinput == "9":
            break
        if userinput == "1":
            get_all_pokemon()
            break


def get_all_pokemon():

    r = requests.get("https://pokeapi.co/api/v2/pokemon?limit=200")

    response = r.json()
    # print(response["results"])
    pokemon_list = sorted([pokemon["name"] for pokemon in response["results"]])
    print("------ Lista Pokemonów ------")
    ent = 0
    for pokemon in pokemon_list:
        print(pokemon, end=', ')
        if ent == 7:
            print("")
            ent = 0
        ent = ent + 1
    print("\n-----------------------")
