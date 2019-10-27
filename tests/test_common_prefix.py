import os
import sys

# ensures pytest will locate project without having to run setup.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.common_prefix import CommonPrefix

test_data1 = [
    (["flower", "flow", "flight"], "fl"),
    (["dog", "racecar", "car"], ""),
    (["", "", ""], ""),
    (["leets", "leetcode", "leet", "leeds"], "lee"),
    ([],"")
]

@pytest.mark.parametrize('test_value,expected', test_data1)
def test_solution1(test_value, expected):
    """Tests correctness of largest common prefix."""
    sample = CommonPrefix()
    assert sample.solution1(test_value) == expected

@pytest.mark.parametrize('test_value,expected', test_data1)
def test_solution2(test_value, expected):
    """Tests correctness of largest common prefix."""
    sample = CommonPrefix()
    assert sample.solution2(test_value) == expected

