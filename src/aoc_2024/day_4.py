from src.aoc_2024.helpers import file_reader


class Day4:
    WORD_TARGET = 'XMAS'

    # Get possibles directions we can move from the given cell:
    # DELTAS = [(-1, -1), (-1, 0), (-1, 1),
    #           (0, -1),    X,    (0, 1),
    #           (1, -1), (1, 0), (1, 1)]
    DIRECTION_DELTAS = [(y,x) for y in [-1, 0, 1] for x in [-1, 0 ,1] if (x != 0 or y !=0)]

    def __init__(self, filename):
        self.word_search = file_reader.get_lines(filename)
        self.rows = len(self.word_search)
        self.columns = len(self.word_search[0])

        self.grid = {(y,x): self.word_search[y][x] for y in range(self.rows) for x in range(self.columns)}

    def part_1(self):
        total_occurences = 0

        for y, x in self.grid:
            # Check foreach direction possible
            for direction_y, direction_x in self.DIRECTION_DELTAS:
                word = "".join(self.grid.get((y + direction_y * i, x + direction_x * i), "") for i in range(len(self.WORD_TARGET)))

                if word == self.WORD_TARGET:
                    total_occurences += 1

        return total_occurences


    def part_2(self):
        total_occurences = 0

        for y, x in self.grid:
            # Find 'A' to check the patterns around it
            if self.grid[y,x] == 'A':
                # Check position (-1, -1) to (1, 1)
                top_to_bottom_right_diagonal = self.grid.get((y-1, x-1), "") + self.grid.get((y+1, x+1), "")
                bottom_to_top_right_diagonal = self.grid.get((y-1, x+1), "") + self.grid.get((y+1, x-1), "")

                if top_to_bottom_right_diagonal in ['MS', 'SM'] and bottom_to_top_right_diagonal in ['MS', 'SM']:
                    total_occurences += 1

        return total_occurences


def main():
    day_4 = Day4(filename="day_4.txt")

    print('Advent of Code 2024 : Day 4')
    print('===========================')
    print('Part 1')
    print(f"XMAS occurs {day_4.part_1()} times")
    print('Part 2')
    print(f"XMas occurs {day_4.part_2()} times")


if __name__ == "__main__":
    main()