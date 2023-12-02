from aoc_2023.helpers import file_reader

RED = "red"
GREEN = "green"
BLUE = "blue"

MAX_CUBES_NUMBER_BY_COLOR = {
    RED: 12,
    GREEN: 13,
    BLUE: 14
}

def main():
    print('Advent of Code 2023 : Day 2')
    print('===========================')
    print('Part 1')
    print(f"Sum of possible games: {_part_1()}")
    print('Part 2')
    print(f"Sum of possible games: {_part_2()}")


def _part_1():
    games = file_reader.get_lines("day_2.txt")
    possible_games_ids = []

    for game in games:
        game_cubes = game.split(":")[1]
        cube_sets = game_cubes.split(";")

        if _is_cube_sets_possibles(cube_sets):
            game_id = _get_number_in_string(game.split(":")[0])
            possible_games_ids.append(game_id)

    return sum(possible_games_ids)


def _part_2():
    games = file_reader.get_lines("day_2.txt")
    cube_set_power = []

    for game in games:
        game_cubes = game.split(":")[1]
        cube_sets = game_cubes.split(";")
        cube_set_power.append(_determine_sets_power(cube_sets))

    return sum(cube_set_power)


def _determine_sets_power(cube_sets):
    max_red_in_set = 0
    max_green_in_set = 0
    max_blue_in_set = 0

    for cube_set in cube_sets:
        for cubes in cube_set.split(","):
            if RED in cubes:
                red_cubes = _get_number_in_string(cubes)
                if red_cubes > max_red_in_set:
                    max_red_in_set = red_cubes
            elif GREEN in cubes:
                green_cubes = _get_number_in_string(cubes)
                if green_cubes > max_green_in_set:
                    max_green_in_set = green_cubes
            elif BLUE in cubes:
                blue_cubes = _get_number_in_string(cubes)
                if blue_cubes > max_blue_in_set:
                    max_blue_in_set = blue_cubes

    return max_red_in_set * max_green_in_set * max_blue_in_set


def _is_cube_sets_possibles(cube_sets):
    is_possible = True

    for cube_set in cube_sets:
        for cubes in cube_set.split(","):
            if RED in cubes:
                red_cubes = _get_number_in_string(cubes)
                if red_cubes > MAX_CUBES_NUMBER_BY_COLOR[RED]:
                    is_possible = False
            elif GREEN in cubes:
                green_cubes = _get_number_in_string(cubes)
                if green_cubes > MAX_CUBES_NUMBER_BY_COLOR[GREEN]:
                    is_possible = False
            elif BLUE in cubes:
                blue_cubes = _get_number_in_string(cubes)
                if blue_cubes > MAX_CUBES_NUMBER_BY_COLOR[BLUE]:
                    is_possible = False

    return is_possible


def _get_number_in_string(value):
    return int("".join(list(filter(str.isdigit, value))))


if __name__ == "__main__":
    main()
