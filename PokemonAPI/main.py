from get_data import get_pokemon
from user_help import get_help
#Menu obsługi skryptu

print("WITAJ! Jakiego pokemona chcesz znaleźć?")
print("(wpisz: 'wyjdz' aby wyjsc) ('help', aby zobaczyć pomoc)")
while True:
    user_input = input("Podaj nazwe Pokemona: ")
    if user_input.lower() == "wyjdz":
        print("-- Bywaj --")
        break
    if user_input.lower() == "help":
        get_help()
    else:
        get_pokemon(user_input)

