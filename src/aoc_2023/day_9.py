from src.aoc_2023.helpers import file_reader


def _part_1(lines):
    next_history_values = []

    for line in lines:
        history_sequence = [int(x) for x in line.split()]
        sequences = _get_current_history_sequences(history_sequence)
        next_history_values.append(_get_last_history_value(sequences))

    return sum(next_history_values)


def _part_2(lines):
    next_history_values = []

    for line in lines:
        history_sequence = [int(x) for x in line.split()]
        sequences = _get_current_history_sequences(history_sequence)
        next_history_values.append(_get_first_history_value(sequences))

    return sum(next_history_values)


def _get_current_history_sequences(history_sequence):
    sequences = []
    current_sequence = history_sequence
    is_last_sequence = False

    while not is_last_sequence:
        sequences.append(current_sequence)

        if all(x == 0 for x in current_sequence):
            is_last_sequence = True
        else:
            current_sequence = [y - x for x, y in zip(current_sequence, current_sequence[1:])]

    return sequences


def _get_last_history_value(sequences):
    next_sequence_value = 0

    while len(sequences) > 0:
        current_sequence = sequences.pop()
        if len(sequences) == 0:
            return next_sequence_value
        else:
            next_sequence_value = sequences[-1][-1] + current_sequence[-1]
            sequences[-1].append(next_sequence_value)

    return next_sequence_value


def _get_first_history_value(sequences):
    next_sequence_value = 0

    while len(sequences) > 0:
        current_sequence = sequences.pop()
        if len(sequences) == 0:
            return next_sequence_value
        else:
            next_sequence_value = sequences[-1][0] - current_sequence[0]
            sequences[-1].insert(0, next_sequence_value)

    return next_sequence_value


def main():
    print('Advent of Code 2023 : Day 9')
    print('===========================')
    print('Part 1')
    print(f"Result: {_part_1(file_reader.get_lines('day_9.txt'))}")
    print('Part 2')
    print(f"Result: {_part_2(file_reader.get_lines('day_9.txt'))}")


if __name__ == "__main__":
    main()
