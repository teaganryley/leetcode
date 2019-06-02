class IsPalindrome:
    """
        Solution which allows conversion to string.
        Note:
            -problem definition excludes negative numbers from being palindromes.
            -single-digit numbers are considered palindromes.
    """
    def solution1(self, num):
        # test for sign
        if num < 0:
            return False
        else:
            return str(num) == str(num)[::-1]

