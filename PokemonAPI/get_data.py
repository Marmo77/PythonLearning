import requests

def get_pokemon(pokemon_name: str):

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"

    response = requests.get(url)

    if response.status_code == 404:
        print(f"Przykro nam, nie znaleźliśmy twojego pokemona o nazwie: {pokemon_name} :(\n")
        return

    data = response.json()

    #------------------------
    poke_id: int = data["id"]
    name: str = data["name"].capitalize()
    weight_kg = f"{data["weight"] / 10} kg"
    height_m = f"{data["height"] / 10} m"
    abilities_list = [ability["ability"]["name"] for ability in data["abilities"]]
    types_list = [type["type"]["name"] for type in data["types"]]
    #------------------------
    print_pokemon_data(poke_id, name, abilities_list, types_list, weight_kg, height_m)
    return

def print_pokemon_data(poke_id, name, abilities, types, weight, height):

    abilities_str = ", ".join(str(ab) for ab in abilities)
    types_str = ", ".join(str(tp) for tp in types)

    print("-" * 20)
    print(f"🌟Nazwa: {name} (#{poke_id})")
    print(f"📏Wzrost: {height}, Waga: {weight}")
    print(f"✊Umiejętności: {abilities_str}")
    print(f"🔥Typ: {types_str}")
    print("-" * 20)