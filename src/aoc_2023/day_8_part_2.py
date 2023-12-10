import math

from src.aoc_2023.day_8_part_1 import _map_nodes
from src.aoc_2023.helpers import file_reader


def _part_2(lines):
    lines.remove('')

    directions = lines[0]
    nodes = _map_nodes(lines[1:])

    steps = []

    starting_nodes = {key: nodes[key] for key in nodes if key.endswith('A')}

    for starting_node in starting_nodes:
        i = 0
        current_node = starting_node

        while not current_node.endswith('Z'):
            current_direction = directions[i % len(directions)]
            i += 1

            if current_direction == 'L':
                current_node = nodes[current_node][0]
            else:
                current_node = nodes[current_node][1]

        steps.append(i)

    return math.lcm(*steps)


def main():
    print('Advent of Code 2023 : Day 8')
    print('===========================')
    print('Part 2')
    print(f"Result: {_part_2(file_reader.get_lines('day_8.txt'))}")


if __name__ == "__main__":
    main()
