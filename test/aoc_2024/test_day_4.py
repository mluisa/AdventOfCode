from src.aoc_2024.day_4 import Day4


def test__day4__part1__should_occurs_18_times():
    assert Day4('sample_day_4.txt').part_1() == 18

def test__day4__part2__should_occurs_9_times():
    assert Day4('sample_day_4_part_2.txt').part_2() == 9