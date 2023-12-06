from src.aoc_2023.helpers import file_reader


def _part_1(filename: str) -> int:
    cards = file_reader.get_lines(filename)
    points = 0

    for card in cards:
        game_numbers, winning_numbers = _read_game(card)
        winning_numbers_count = len(_get_matching_numbers(game_numbers, winning_numbers))

        if winning_numbers_count > 0:
            points += pow(2, winning_numbers_count - 1)

    return points


def _part_2(filename: str) -> int:
    cards = file_reader.get_lines(filename)
    cards_copy = _get_total_cards_instance(cards)

    return sum(cards_copy.values())


def _get_matching_numbers(game_numbers: list, winning_numbers: list) -> list:
    return [
        x
        for x in winning_numbers.split(' ')
        if x in game_numbers.split(' ') and x != ''
    ]


def _read_game(card: str):
    card_id, card_game = card.split(":")
    winning_numbers, game_numbers = card_game.split('|')

    return game_numbers, winning_numbers


def _get_total_cards_instance(cards):
    total_cards = len(cards)
    cards_copy = dict(((i + 1, 1) for i in range(total_cards)))

    for i in range(0, len(cards_copy)):
        game_numbers, winning_numbers = _read_game(cards[i])
        winning_numbers_count = len(_get_matching_numbers(game_numbers, winning_numbers))

        if winning_numbers_count > 0:
            current_total_cards = cards_copy[i + 1]
            for j in range(i + 1, i + winning_numbers_count + 1):
                cards_copy[j + 1] += current_total_cards

    return cards_copy


def main():
    print('Advent of Code 2023 : Day 4')
    print('===========================')
    print('Part 1')
    print(f"Total cards points: {_part_1('day_4.txt')}")
    print('Part 2')
    print(f"Total card instances: {_part_2('day_4.txt')}")


if __name__ == "__main__":
    main()
