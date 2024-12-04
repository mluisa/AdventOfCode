from src.aoc_2024.helpers import file_reader

class ReportAnalyzer:
    @classmethod
    def get_safe_reports_count(cls, reports, with_dampener=False):
        safe_reports = 0
        for report in reports:
            levels = [int(level) for level in report.split()]
            if cls._is_safe_report(levels, with_dampener):
                safe_reports += 1

        return safe_reports

    @classmethod
    def _is_safe_report(cls, levels, with_dampener):
        if cls._validate_safety(levels):
            return True

        if not with_dampener:
            return False

        return cls._can_become_safe_by_removing_one(levels)

    @classmethod
    def _validate_safety(cls, levels):
        is_increasing = levels[0] < levels[1] if len(levels) > 1 else True

        for i in range(1, len(levels)):
            if is_increasing:
                if levels[i - 1] > levels[i]:
                    return False
            else:
                if levels[i - 1] < levels[i]:
                    return False

            if levels[i - 1] == levels[i] or abs(levels[i - 1] - levels[i]) not in [1, 2, 3]:
                return False

        return True

    @classmethod
    def _can_become_safe_by_removing_one(cls, levels):
        for i in range(len(levels)):
            modified_levels = levels[:i] + levels[i + 1:]
            if cls._validate_safety(levels=modified_levels):
                return True

        return False

class Day2:
    def __init__(self, filename: str):
        self.reports = file_reader.get_lines(filename=filename)

    def part_1(self):
        return ReportAnalyzer.get_safe_reports_count(self.reports)

    def part_2(self):
        return ReportAnalyzer.get_safe_reports_count(self.reports, with_dampener=True)


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