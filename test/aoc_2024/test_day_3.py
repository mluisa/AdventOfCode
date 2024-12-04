from src.aoc_2024.day_3 import Day3


def test__day3__part_1__should_return_161():
    assert Day3(filename="sample_day_3.txt").part_1() == 161

def test__day3__part_2__should_return_48():
    assert Day3(filename="sample_day_3_part_2.txt").part_2() == 48