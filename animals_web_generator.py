import json
import os


def load_data(file_path: str) -> list:
    """
    Loads data from json file.
    :param file_path:
    :return:
    """
    with open(file_path, "r") as handle:
        all_data = json.load(handle)
        return all_data


def serialize_animal(animal):
    animals_cards = ''

    locations = animal.get('locations', ['Location not found'])
    locations_string = ', '.join(locations)

    animals_cards += '<li class="cards__item">\n'
    animals_cards += ('<div class="card__title">'
                      + animal.get('name', 'Name not found')
                      + '</div>\n')
    animals_cards += '<div class="card__text">'
    animals_cards += '<ul>\n'
    animals_cards += ('<li>'
                      + '<strong>'
                      + 'Diet:'
                      + '</strong>'
                      + ' '
                      + animal.get('characteristics', {}).get('diet', 'Diet not found')
                      + '</li>\n')

    if animal.get('characteristics', {}).get('type') is not None:
        animals_cards += ('<li>'
                          + '<strong>'
                          + 'Type:'
                          + '</strong>'
                          + ' '
                          + animal.get('characteristics', {}).get('type').capitalize()
                          + '</li>\n')

    animals_cards += ('<li>'
                      + '<strong>'
                      + 'Location(s):'
                      + '</strong>'
                      + ' '
                      + f"{locations_string}"
                      + '</li>\n')
    animals_cards += ('<li>'
                      + '<strong>'
                      + 'Lifespan:'
                      + '</strong>'
                      + ' '
                      + animal.get('characteristics', {}).get('lifespan', 'Lifespan not found')
                      + '</li>\n')

    if animal.get('characteristics', {}).get('top_speed') is not None:
        animals_cards += ('<li>'
                          + '<strong>'
                          + 'Top Speed:'
                          + '</strong>'
                          + ' '
                          + animal.get('characteristics', {}).get('top_speed')
                          + '</li>\n')

    animals_cards += '</ul>\n'
    animals_cards += '</div>\n'
    animals_cards += '</li>\n'

    return animals_cards


def get_animal_cards(all_animals: list) -> str:
    """ Prints Name, Diet, Location and Type (if any given) of each animal """
    animals_cards = ''

    for animal in all_animals:
        animals_cards += serialize_animal(animal)

    return animals_cards


def open_template(file_path: str) -> str:
    """ Reads the content of the template file """
    with open(file_path, "r") as handle:
        page_template = handle.read()
        return page_template


def inject_animal_cards(page_template: str, animal_cards: str) -> str:
    """ Injects animal cards into page_template """
    return page_template.replace("__REPLACE_ANIMALS_INFO__", animal_cards)


def build_repository_page(page: str) -> None:
    """ Builds the repository page """
    if not os.path.exists('output'):
        os.mkdir('output')
    file_path = os.path.join('output', 'animals.html')
    with open(file_path, "w") as handle:
        handle.write(page)


def main():
    animals_data = load_data('data/animals_data.json')
    animals_cards = get_animal_cards(animals_data)
    page_template = open_template('templates/animals_template.html')
    new_page_template = inject_animal_cards(page_template, animals_cards)
    build_repository_page(new_page_template)


if __name__ == "__main__":
    main()
