from get_data import get_pokemon

#Menu obsługi skryptu

print("WITAJ! Jakiego pokemona chcesz znaleźć? (wpisz: 'wyjdz' aby wyjsc)\n")
while True:
    user_input = input("Podaj nazwe Pokemona: ")
    if user_input.lower() == "wyjdz":
        break

    get_pokemon(user_input)

