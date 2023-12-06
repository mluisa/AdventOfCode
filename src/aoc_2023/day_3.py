import operator
import re
from functools import reduce

from src.aoc_2023.helpers import file_reader


INVALID_SYMBOL = "."
VALID_SYMBOL = "*"
REGEX_DIGITS_ONLY = re.compile(r"\d+")


def _part_1(filename: str):
    engine_schematic = file_reader.get_lines(filename)
    adjacent_engine_parts = _get_adjacent_parts(engine_schematic)

    return sum([n for n,p in adjacent_engine_parts])


def _part_2(filename: str):
    engine_schematic = file_reader.get_lines(filename)
    adjacent_engine_parts = _get_adjacent_parts(engine_schematic)
    engine_parts = _group_engine_parts_by_position(adjacent_engine_parts)
    parts_products = _get_valid_parts_product(engine_parts)

    return sum(parts_products)


def _get_valid_parts_product(engine_parts):
    parts_products = []
    for position in engine_parts:
        if len(engine_parts[position]) > 1:
            parts_products.append(reduce(operator.mul, engine_parts[position]))
    return parts_products


def _group_engine_parts_by_position(adjacent_engine_parts):
    engine_parts = {}
    for part in adjacent_engine_parts:
        part_value = part[0]
        part_symbol = part[1][0]
        part_position = part[1][1]

        if part_symbol == VALID_SYMBOL:
            engine_parts.setdefault(part_position, []).append(part_value)

    return engine_parts


def _get_adjacent_parts(engine_schematic):
    engine_parts = []

    for i, row_value in enumerate(engine_schematic):
        for match in REGEX_DIGITS_ONLY.finditer(row_value):
            part_number = match.group(0)

            start_position = match.start()
            end_position = match.end()

            adjacent_symbol = []
            for y in range(max(i - 1, 0), min(i + 2, len(engine_schematic))):
                for x in range(max(start_position - 1, 0), min(end_position + 1, len(engine_schematic[i]))):
                    if not engine_schematic[y][x].isdigit() and engine_schematic[y][x] != INVALID_SYMBOL:
                        adjacent_symbol.append((engine_schematic[y][x], (x, y)))

            if len(adjacent_symbol):
                engine_parts.append((int(part_number), adjacent_symbol[0]))

    return engine_parts


def main():
    print('Advent of Code 2023 : Day 2')
    print('===========================')
    print('Part 1')
    print(f"Sum of engine parts: {_part_1('day_3.txt')}")
    print('Part 2')
    print(f"Sum of engine parts: {_part_2('day_3.txt')}")


if __name__ == "__main__":
    main()
