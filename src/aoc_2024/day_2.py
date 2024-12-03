from src.aoc_2024.helpers import file_reader


class Day2:
    def __init__(self, filename: str):
        self.reports = file_reader.get_lines(filename=filename)

    def part_1(self):
        return self._get_safe_reports_count()

    def _get_safe_reports_count(self):
        safe_reports = 0
        for report in self.reports:
            levels = [int(level) for level in report.split()]
            if self._validate_safety(levels=levels):
                safe_reports += 1


        return safe_reports

    def _validate_safety(self, levels):
        is_increasing = levels[0] < levels[1]

        for i in range(1, len(levels)):
            difference = abs(levels[i - 1] - levels[i]) if len(levels) > 1 else 0
            if difference not in [1, 2, 3]:
                return False

            if is_increasing and levels[i - 1] > levels[i]:
                return False

            if not is_increasing and levels[i - 1] < levels[i]:
                return False

        return True

    def part_2(self):
        return self._get_safe_reports_count()


def main():
    day_2 = Day2(filename="day_2.txt")

    print('Advent of Code 2024 : Day 2')
    print('===========================')
    print('Part 1')
    print(f"Total of safe reports: {day_2.part_1()}")
    print('Part 2')
    print(f"Sum of calibration numbers: {day_2.part_2()}")


if __name__ == "__main__":
    main()