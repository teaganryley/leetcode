import os
import sys

# ensures pytest will locate project without having to run setup.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.valid_parentheses import ValidParentheses

test_data1 = [
    ('', True),
    ('()', True),
    ('()[]{}', True),
    ('([)]', False),
    ('){', False)
]


@pytest.mark.parametrize('input_str,expected', test_data1)
def test_s1(input_str, expected):
    sample = ValidParentheses()
    assert sample.solution1(input_str) == expected
