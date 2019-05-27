import os
import sys

# ensures pytest will locate project without having to run setup.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.two_sum import TwoSum

test_data_pass = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 3], 6, [0, 1])
]


@pytest.fixture
def sample_two_sum():
    sample = TwoSum()
    return sample


@pytest.mark.parametrize('nums,target,expected', test_data_pass)
def test_solution_1_pass(sample_two_sum, nums, target, expected):
    """Test correctness of solution1"""
    print('Array: {0} Target: {1} Expected: {2}'.format(nums, target, expected))
    assert sample_two_sum.solution1(nums, target) == expected


@pytest.mark.parametrize('nums,target,expected', test_data_pass)
def test_solution_2_pass(sample_two_sum, nums, target, expected):
    """Test correctness of solution2"""
    print('Array: {0} Target: {1} Expected: {2}'.format(nums, target, expected))
    assert sample_two_sum.solution2(nums, target) == expected
