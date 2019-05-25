class TwoSum:
    """
    Solutions for leetcode "two sum" problem: https://leetcode.com/problems/two-sum/

    Solution 1 takes the naive approach, using a nested loop to test each combination. The indices
    are returned if the two integers add up to the target.

    Solution 2 uses a single loop to iterate through the array, determining the complement of the
    current integer, then searching for it in a dictionary (or hash table, depending on implementation).
    """

    def solution1(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def solution2(self, nums, target):
        pairs = []
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in pairs:
                return [pairs.index(complement), i]
            pairs.append(nums[i])

