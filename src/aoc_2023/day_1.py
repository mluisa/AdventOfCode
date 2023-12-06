from src.aoc_2023.helpers import file_reader


NUMBER_EQUIVALENCES = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def main():
    print('Advent of Code 2023 : Day 1')
    print('===========================')
    print('Part 1')
    print(f"Sum of calibration numbers: {_part_1()}")
    print('Part 2')
    print(f"Sum of calibration numbers: {_part_2()}")


def _part_1():
    calibration_instructions = file_reader.get_lines(filename="day_1.txt")
    return _get_calibration_instructions_sum(calibration_instructions)


def _part_2():
    calibration_instructions = file_reader.get_lines(filename="day_1.txt")

    decoded_calibration_instructions = []
    for instruction in calibration_instructions:
        instruction_numbers = _find_digits_in_instruction(instruction)
        decoded_calibration_instructions.append(instruction_numbers)

    return _get_calibration_instructions_sum(decoded_calibration_instructions)


def _find_digits_in_instruction(instruction):
    instruction_numbers = ""

    for i in range(len(instruction)):
        if instruction[i].isdigit():
            instruction_numbers += instruction[i]
        else:
            for equivalence, number in NUMBER_EQUIVALENCES.items():
                if instruction[i:].startswith(equivalence):
                    instruction_numbers += str(number)

    return instruction_numbers


def _get_calibration_instructions_sum(calibration_instructions):
    calibration_numbers = []

    for instruction in calibration_instructions:
        digits = [c for c in instruction if c.isdigit()]
        calibration_number = int(digits[0] + digits[-1])
        calibration_numbers.append(calibration_number)

    return sum(calibration_numbers)


if __name__ == "__main__":
    main()
