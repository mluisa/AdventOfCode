import re

from src.aoc_2024.helpers import file_reader


class Day3:
    VALID_INSTRUCTION_REGEX = re.compile(r'mul\((\d+),(\d+)\)')
    DO_NOT_EXECUTE_INSTRUCTIONS_REGEX = re.compile(r"don't\(\)")
    DO_EXECUTE_INSTRUCTIONS_REGEX = re.compile(r"do\(\)")

    SEQUENCE_PATTERNS = [
        VALID_INSTRUCTION_REGEX,
        DO_NOT_EXECUTE_INSTRUCTIONS_REGEX,
        DO_EXECUTE_INSTRUCTIONS_REGEX
    ]

    def __init__(self, filename: str):
        self.instructions = "".join(file_reader.get_lines(filename=filename))

    def part_1(self):
        products = []
        products.extend([int(x) * int(y) for x, y in re.findall(self.VALID_INSTRUCTION_REGEX, self.instructions)])
        return sum(products)

    def part_2(self):
        valid_sequence = []
        position = 0

        while position < len(self.instructions):
            matched = False

            for pattern in self.SEQUENCE_PATTERNS:
                match = pattern.match(self.instructions, position)

                if match:
                    if pattern == self.VALID_INSTRUCTION_REGEX:
                        valid_sequence.append((int(match.group(1)), int(match.group(2))))
                        position = match.end()  # Move position after the match
                        matched = True
                        break
                    elif pattern == self.DO_NOT_EXECUTE_INSTRUCTIONS_REGEX:
                        valid_sequence.append(match.group(0))
                        position = match.end()  # Move position after the match
                        matched = True
                        break
                    elif pattern == self.DO_EXECUTE_INSTRUCTIONS_REGEX:
                        valid_sequence.append(match.group(0))
                        position = match.end()  # Move position after the match
                        matched = True
                        break

            if not matched:
                position += 1

        products = []
        ignore_instruction = False
        for instruction in valid_sequence:
            if isinstance(instruction, tuple) and not ignore_instruction:
                products.append(instruction[0] * instruction[1])
                continue

            if not isinstance(instruction, tuple) and re.match(self.DO_NOT_EXECUTE_INSTRUCTIONS_REGEX, instruction):
                ignore_instruction = True

            if not isinstance(instruction, tuple) and re.match(self.DO_EXECUTE_INSTRUCTIONS_REGEX, instruction):
                ignore_instruction = False


        return sum(products)


def main():
    day_3 = Day3(filename="day_3.txt")

    print('Advent of Code 2024 : Day 3')
    print('===========================')
    print('Part 1')
    print(f"Sum of the results: {day_3.part_1()}")
    print('Part 2')
    print(f"Sum of the results: {day_3.part_2()}")


if __name__ == "__main__":
    main()