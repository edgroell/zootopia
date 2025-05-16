import json


def load_data(file_path: str) -> list:
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        all_data = json.load(handle)
        return all_data


def print_animals(all_animals: list) -> None:
    """ Prints Name, Diet, Location and Type (if any given) of each animal """
    for animal in all_animals:
        print(f"Name: {animal.get('name', 'Name not found')}")
        print(f"Diet: {animal.get('characteristics', {}).get('diet', 'Diet not found')}")
        print(f"Location: {animal.get('locations', 'Location not found')[0]}")

        if animal.get('characteristics', {}).get('type') is not None:
            print(f"Type: {animal.get('characteristics', {}).get('type').capitalize()}")

        print("")


def main():
    animals_data = load_data('animals_data.json')
    print_animals(animals_data)


if __name__ == "__main__":
    main()
