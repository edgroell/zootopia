import json


def load_data(file_path: str) -> list:
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        all_data = json.load(handle)
        return all_data


def get_animal_cards(all_animals: list) -> str:
    """ Prints Name, Diet, Location and Type (if any given) of each animal """
    animals_cards = ''

    for animal in all_animals:
        animals_cards += '<li class="cards__item">'
        animals_cards += f"Name: {animal.get('name', 'Name not found')}<br/>\n"
        animals_cards += f"Diet: {animal.get('characteristics', {}).get('diet', 'Diet not found')}<br/>\n"
        #animals_cards += f"Location: {animal.get('locations', 'Location not found')[0]}<br/>\n"
        locations = animal.get('locations', ['Location not found'])
        locations_string = ', '.join(locations)
        animals_cards += f"Location(s): {locations_string}<br/>\n"

        if animal.get('characteristics', {}).get('type') is not None:
            animals_cards += f"Type: {animal.get('characteristics', {}).get('type').capitalize()}<br/>\n"

        animals_cards += f"</li>"

    return animals_cards


def open_template(file_path: str) -> str:
    """ Reads the content of the template file """
    with open(file_path, "r") as handle:
        page_template = handle.read()
        return page_template


def inject_animal_cards(page_template: str, animal_cards: str) -> str:
    """ Injects animal cards into page_template """
    return page_template.replace("__REPLACE_ANIMALS_INFO__", animal_cards)


def build_repository_page(page: str) -> str:
    """ Builds the repository page """
    with open("animals.html", "w") as handle:
        handle.write(page)


def main():
    animals_data = load_data('animals_data.json')
    animals_cards = get_animal_cards(animals_data)
    page_template = open_template('animals_template.html')
    new_page_template = inject_animal_cards(page_template, animals_cards)
    build_repository_page(new_page_template)


if __name__ == "__main__":
    main()
