import json
import os


def load_data(file_path: str) -> list:
    """
    Loads data from json file.
    :param file_path: str indicating the path to the json file
    :return: all_data: list containing all data from the json file
    """
    with open(file_path, "r") as handle:
        all_data = json.load(handle)

        return all_data


def serialize_animal(animal: dict) -> str:
    """
    Builds the entire string in html format for a given animal.
    :param animal: dict containing all data from given animal.
    :return: animals_cards: str containing all info of a given animal in html format.
    """
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
    """
    Builds the entire string in html format for all animals.
    :param all_animals: list containing all info from all animals.
    :return: animals_cards: str containing all info of all animals in html format.
    """
    animals_cards = ''

    for animal in all_animals:
        animals_cards += serialize_animal(animal)

    return animals_cards


def open_template(file_path: str) -> str:
    """
    Reads the content of the html template file.
    :param file_path: str indicating the path to the html template file.
    :return: page_template: str containing all info from the html template file.
    """
    with open(file_path, "r") as handle:
        page_template = handle.read()

        return page_template


def inject_animal_cards(page_template: str, animal_cards: str) -> str:
    """
    Replaces the placeholder from the html template with data extracted from the json file (i.e., the animal cards).
    :param page_template: str containing all info from the html template file.
    :param animal_cards: str containing all info from all animals in html format.
    :return: final_page_content: str containing the final page in html format.
    """
    final_page_content = page_template.replace("__REPLACE_ANIMALS_INFO__", animal_cards)

    return final_page_content


def build_repository_page(final_content: str) -> None:
    """
    Builds the final html page containing the animal cards.
    :param final_content: str containing the final page in html format.
    :return: None
    """
    if not os.path.exists('output'):
        os.mkdir('output')

    file_path = os.path.join('output', 'animals.html')

    with open(file_path, "w") as handle:
        handle.write(final_content)


def main():
    animals_data = load_data(os.path.join('data', 'animals_data.json'))
    animals_cards = get_animal_cards(animals_data)
    page_template = open_template(os.path.join('templates', 'animals_template.html'))
    final_page_content = inject_animal_cards(page_template, animals_cards)
    build_repository_page(final_page_content)


if __name__ == "__main__":
    main()
