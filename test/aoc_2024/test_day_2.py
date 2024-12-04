import pytest

from src.aoc_2024.day_2 import Day2, ReportAnalyzer


# 356
def test__part_1__should_return_2_safe_reports():
    assert Day2(filename="sample_day_2.txt").part_1() == 2

def test__part_2__should_return_4_safe_reports():
    assert Day2(filename="sample_day_2.txt").part_2() == 4

@pytest.mark.parametrize(
    "levels, expected",
    [
        ([7,6,4,2,1], True),
        ([1,2,7,8,9], False),
        ([9,7,6,2,1], False),
        ([1,3,2,4,5], False),
        ([8,6,4,4,1], False),
        ([1,3,6,7,9], True)
    ]
)
def test__validate_safety__without_tolerate_bad_level__should_return_expected(levels, expected):
    report_analyzer = ReportAnalyzer

    result = report_analyzer._validate_safety(levels)

    assert result == expected

@pytest.mark.parametrize(
    "levels, expected",
    [
        ([7,6,4,2,1], True),
        ([1,2,7,8,9], False),
        ([9,7,6,2,1], False),
        ([1,3,2,4,5], True),
        ([8,6,4,4,1], True),
        ([1,3,6,7,9], True)
    ]
)
def test__can_become_safe_by_removing_one__with_tolerate_bad_level__should_return_expected(levels, expected):
    report_analyzer = ReportAnalyzer()

    result = report_analyzer._can_become_safe_by_removing_one(levels)

    assert result == expected