import pytest
from largest_possible_number import LargestNumber

def test_case_one():
    l = LargestNumber([50, 2, 1, 9])
    assert l.get_result() == '95021'

def test_case_two():
    l = LargestNumber([9, 199, 5, 2, 0, 0, 6])
    assert l.get_result() == '965219900'