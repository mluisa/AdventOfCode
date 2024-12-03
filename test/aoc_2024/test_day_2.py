import pytest

from src.aoc_2024.day_2 import Day2

# 356
def test__part_1__should_return_2_safe_reports():
    assert Day2(filename="sample_day_2.txt").part_1() == 2

def test__part_2__should_return_4_safe_reports():
    assert Day2(filename="sample_day_2.txt").part_2() == 4