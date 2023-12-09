import math

from src.aoc_2023.helpers import file_reader

STARTING_BOAT_SPEED = 0  # 0 mm per milliseconds
SPEED_UP_PER_SECOND = 1  # 1 mm per milliseconds


def _part_1(lines):
    times = [int(x) for x in lines[0].split()[1:]]
    distances = [int(x) for x in lines[1].split()[1:]]
    races_options_to_win_count = _get_races_options_to_win_count(distances, times)

    return math.prod(races_options_to_win_count)


def _part_2(lines):
    times = [int(lines[0].split(':')[1:][0].replace(' ', ''))]
    distances = [int(lines[1].split(':')[1:][0].replace(' ', ''))]
    races_options_to_win_count = _get_races_options_to_win_count(distances, times)

    return math.prod(races_options_to_win_count)


def _get_races_options_to_win_count(distances, times):
    races_options_to_win_count = []

    for index, time in enumerate(times):
        distance = distances[index]

        race_options = []
        for i in range(1, time):
            remaining_time = time - i
            final_distance = (remaining_time * (i * SPEED_UP_PER_SECOND))
            if final_distance > distance:
                race_options.append(i)

        races_options_to_win_count.append(len(race_options))

    return races_options_to_win_count


def main():
    print('Advent of Code 2023 : Day 6')
    print('===========================')
    print('Part 1')
    print(f"Result: {_part_1(file_reader.get_lines('day_6.txt'))}")
    print('Part 2')
    print(f"Result: {_part_2(file_reader.get_lines('day_6.txt'))}")


if __name__ == "__main__":
    main()
