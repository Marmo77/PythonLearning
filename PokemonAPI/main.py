from get_data import get_pokemon
from user_help import get_all_pokemon
#Menu obsługi skryptu


def menuList():
    print("----- Menu -----")
    print("1. Pokemon")
    print("2. Lista Pokemonów")
    print("3. X")
    print("9. wyjdz")
    print("-----------------")


def start():
    print("----- WITAJ W CENTRUM POKEMONÓW -----")
    print("wybierz numer z listy:")
    while True:
        menuList()
        user_input = input("> ")
        if user_input == "1":
            while True:
                print("---- Podaj nazwe Pokemona ----")
                print("(wpisz 'wyjdz', aby wrócić do Menu)")
                pokemon_name = input("Pokemon: ").lower()
                if pokemon_name == "wyjdz":
                    break

                get_pokemon(pokemon_name)

        if user_input.lower() == "2":
            get_all_pokemon()

        if user_input.lower() == "9":
            print("-- Bywaj --")
            break


if __name__ == "__main__":
    start()