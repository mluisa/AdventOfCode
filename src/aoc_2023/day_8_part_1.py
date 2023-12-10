from src.aoc_2023.helpers import file_reader

START_NODE = 'AAA'
ENDING_NODE = 'ZZZ'


def _map_nodes(lines):
    nodes = {}

    for line in lines:
        node = line.replace(' ' , '').split('=')
        left_value = node[1].split(',')[0].replace('(', '')
        right_value = node[1].split(',')[1].replace(')', '')
        nodes[node[0]] = (left_value, right_value)

    return nodes


def _part_1(lines):
    lines.remove('')

    directions = lines[0]
    nodes = _map_nodes(lines[1:])

    i = 0
    current_node = START_NODE
    while current_node != ENDING_NODE:
        current_direction = directions[i % len(directions)]
        i += 1

        if current_direction == 'L':
            current_node = nodes[current_node][0]
        else:
            current_node = nodes[current_node][1]

    return i


def main():
    print('Advent of Code 2023 : Day 8')
    print('===========================')
    print('Part 1')
    print(f"Result: {_part_1(file_reader.get_lines('day_8.txt'))}")


if __name__ == "__main__":
    main()
