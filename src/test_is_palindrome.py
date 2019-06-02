import os
import sys

# ensures pytest will locate project without having to run setup.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.is_palindrome import IsPalindrome


test_cases1 = [
    (121, True),
    (0, True),
    (1, True),
    (-121, False),
    (10, False)
]


@pytest.mark.parametrize('num,expected', test_cases1)
def test_s1(num, expected):
    """Tests correctness, boundaries, and failure of IsPalindrome"""
    sample = IsPalindrome()
    assert sample.solution1(num) == expected

