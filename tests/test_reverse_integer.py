import os
import sys

# ensures pytest will locate project without having to run setup.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.reverse_integer import ReverseInteger

s1_correct = [
    (123, 321),
    (-123, -321),
    (120, 21),
    (-120, -21),
    (0, 0),
    ((2 ** 31) - 1, 0),
    (-2 ** 31, 0),
    (2 ** 34, 0),
    (-2 ** 33, 0)
]


@pytest.fixture
def sample_ri():
    sample = ReverseInteger()
    return sample


@pytest.mark.parametrize('num,expected', s1_correct)
def test_s1_correctness(sample_ri, num, expected):
    """Tests correctness of reverse integer solution."""
    assert sample_ri.solution1(num) == expected

