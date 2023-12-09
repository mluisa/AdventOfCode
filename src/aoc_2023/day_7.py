from src.aoc_2023.helpers import file_reader

HANDS = [
    [5],  # Five of a kind
    [4, 1],  # Four of a kind
    [3, 2],  # Full house
    [3, 1, 1],  # Three of a kind
    [2, 2, 1],  # Two pairs
    [2, 1, 1, 1],  # One pair
    [1, 1, 1, 1, 1]  # High card
]

CARDS_PART_1 = 'AKQJT98765432'  # Ordered by the highest to the lowest card value
CARDS_PART_2 = 'AKQT98765432J'  # Ordered by the highest to the lowest card value


def _get_hand_type(hand, is_part_2=False):
    if is_part_2:
        hand_recurrence = [hand.count(card) for card in set(hand) if card != 'J']
        hand_recurrence.sort(reverse=True)

        jokers_count = hand.count('J')
        if jokers_count == 5:
            # Return Five of a kind
            return 0
        elif jokers_count != 0:
            # Increment the higher recurrence of a card by jokers present in hand.
            hand_recurrence[0] += hand.count('J')
    else:
        hand_recurrence = [hand.count(card) for card in set(hand)]
        hand_recurrence.sort(reverse=True)

    return HANDS.index(hand_recurrence)


def _part_1(lines):
    hands = [x.split()[0] for x in [line for line in lines]]
    bids = [x.split()[1] for x in [line for line in lines]]

    hands_info = []
    for index, hand in enumerate(hands):
        hand_type = _get_hand_type(hand)
        hands_info.append(
            [
                hand_type,
                list(CARDS_PART_1.index(card) for card in hand),
                int(bids[index])
            ]
        )

    hands_info.sort(reverse=True)

    return sum([(rank+1) * hand[2] for rank, hand in enumerate(hands_info)])


def _part_2(lines):
    hands = [x.split()[0] for x in [line for line in lines]]
    bids = [x.split()[1] for x in [line for line in lines]]

    hands_info = []
    for index, hand in enumerate(hands):
        hand_type = _get_hand_type(hand, True)
        hands_info.append(
            [
                hand_type,
                list(CARDS_PART_2.index(card) for card in hand),
                int(bids[index])
            ]
        )

    hands_info.sort(reverse=True)

    return sum([(rank+1) * hand[2] for rank, hand in enumerate(hands_info)])


def main():
    print('Advent of Code 2023 : Day 7')
    print('===========================')
    print('Part 1')
    print(f"Result: {_part_1(file_reader.get_lines('day_7.txt'))}")
    print('Part 2')
    print(f"Result: {_part_2(file_reader.get_lines('day_7.txt'))}")


if __name__ == "__main__":
    main()
