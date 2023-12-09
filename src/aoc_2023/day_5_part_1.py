from typing import Iterable

from src.aoc_2023.helpers import file_reader

SEPARATOR = ":"
SPACE = " "

SEEDS = "seeds"
SEED_TO_SOIL = "seed-to-soil"
SOIL_TO_FERTILIZER = "soil-to-fertilizer"
FERTILIZER_TO_WATER = "fertilizer-to-water"
WATER_TO_LIGHT = "water-to-light"
LIGHT_TO_TEMPERATURE = "light-to-temperature"
TEMPERATURE_TO_HUMIDITY = "temperature-to-humidity"
HUMIDITY_TO_LOCATION = "humidity-to-location"

DESTINATION_RANGE_START_INDEX = 0
SOURCE_RANGE_START_INDEX = 1
RANGE_LENGTH_INDEX = 2


def _get_seeds(almanac: Iterable[str]) -> list[int]:
    seeds_line = next(x for x in almanac if x.startswith(SEEDS))
    return _get_list_of_elements_from_line(seeds_line.split(SEPARATOR)[1])


def _get_almanac_map_by_map_name(almanac: list[str], map_name: str) -> list[list[int]]:
    start_index = 0

    for index, instruction in enumerate(almanac):
        if instruction.startswith(map_name):
            start_index = index + 1
            break

    seed_to_soil_map = []
    for i in range(start_index, len(almanac)):
        if almanac[i] == '':
            break

        seed_to_soil_map.append(_get_list_of_elements_from_line(almanac[i]))

    return seed_to_soil_map


def _get_list_of_elements_from_line(line: str) -> list[int]:
    return [int(seed) for seed in (line.split(SPACE)) if seed.isdigit()]


def _get_seed_destination(given_source: int, seed_map: list[list[int]]) -> int:
    for instruction in seed_map:
        start_source = instruction[SOURCE_RANGE_START_INDEX]

        if start_source <= given_source <= start_source + instruction[RANGE_LENGTH_INDEX]:
            # Get index where we found the match
            start_destination = instruction[DESTINATION_RANGE_START_INDEX]
            return start_destination + (given_source - start_source)

    # If there is no match, we return the same given number
    return given_source


def _get_almanac_maps(almanac: list[str]) -> list[list[list[int]]]:
    seed_to_soil_map = _get_almanac_map_by_map_name(almanac, SEED_TO_SOIL)
    soil_to_fertilizer_map = _get_almanac_map_by_map_name(almanac, SOIL_TO_FERTILIZER)
    fertilizer_to_water_map = _get_almanac_map_by_map_name(almanac, FERTILIZER_TO_WATER)
    water_to_light_map = _get_almanac_map_by_map_name(almanac, WATER_TO_LIGHT)
    light_to_temperature_map = _get_almanac_map_by_map_name(almanac, LIGHT_TO_TEMPERATURE)
    temperature_to_humidity_map = _get_almanac_map_by_map_name(almanac, TEMPERATURE_TO_HUMIDITY)
    humidity_to_location_map = _get_almanac_map_by_map_name(almanac, HUMIDITY_TO_LOCATION)

    return [
        seed_to_soil_map,
        soil_to_fertilizer_map,
        fertilizer_to_water_map,
        water_to_light_map,
        light_to_temperature_map,
        temperature_to_humidity_map,
        humidity_to_location_map
    ]


def _get_lowest_location(seeds: list[int], seed_maps: list[list[list[int]]]) -> int:
    lowest_location = None

    for seed in seeds:
        current_location = seed
        for seed_map in seed_maps:
            current_location = _get_seed_destination(current_location, seed_map)

        if lowest_location is None or current_location < lowest_location:
            lowest_location = current_location

    return lowest_location


def _get_seeds_from_range(almanac):
    seeds = _get_seeds(almanac)
    seeds_range = (lambda s, n=2: [seeds[i:i + n] for i in range(0, len(seeds), n)])(seeds)

    seeds_number = []
    for seed_range in seeds_range:
        seeds_number.extend([[x for x in range(seed_range[0], seed_range[0] + seed_range[1])]])

    return seeds_number


def _part_1(almanac: list[str]) -> int:
    seeds = _get_seeds(almanac)
    seed_maps = _get_almanac_maps(almanac)

    return _get_lowest_location(seeds, seed_maps)


def main():
    almanac = file_reader.get_lines('day_5.txt')

    print('Advent of Code 2023 : Day 5')
    print('===========================')
    print('Part 1')
    print(f"Lowest location: {_part_1(almanac)}")


if __name__ == "__main__":
    main()
