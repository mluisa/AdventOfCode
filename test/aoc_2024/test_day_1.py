from src.aoc_2024.day_1 import Day1

def test__part_1__returns_11_as_total_distance():
    assert Day1(filename="sample_day_1.txt").part_1() == 11

def test__part_2__return_31_as_similarity_score():
    assert Day1(filename="sample_day_1.txt").part_2() == 31