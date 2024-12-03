from src.aoc_2024.helpers import file_reader


class Day1:

    def __init__(self, filename: str):
        self.data = file_reader.get_lines(filename=filename)

    def part_1(self) -> int:
        first_list, second_list = self.split_in_two_list()

        first_list.sort()
        second_list.sort()

        return sum([abs(x - y) for x, y in zip(first_list, second_list)])


    def part_2(self) -> int:
        first_list, second_list = self.split_in_two_list()

        similarities = []
        for i in range(len(first_list)):
            similarities.append((first_list[i], second_list.count(first_list[i])))

        return sum([x * y for x, y in similarities])


    def split_in_two_list(self):
        first_list = []
        second_list = []

        for line in self.data:
            first, second = map(int, line.split())
            first_list.append(first)
            second_list.append(second)

        return first_list, second_list


def main():
    day_1 = Day1(filename="day_1.txt")

    print('Advent of Code 2024 : Day 1')
    print('===========================')
    print('Part 1')
    print(f"Total distance: {day_1.part_1()}")
    print('Part 2')
    print(f"Similarities: {day_1.part_2()}")


if __name__ == "__main__":
    main()
