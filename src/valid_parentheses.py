class ValidParentheses:
    """
    Solutions for: https://leetcode.com/problems/valid-parentheses
    """

    lh_brace = {'(', '[', '{'}
    rh_brace = {')', ']', '}'}

    brace_pairs = {'()', '[]', '{}'}

    def solution1(self, my_string):
        stack = []

        if len(my_string) % 2 == 1:
            return False
        elif my_string == '':
            return True
        else:
            for char in my_string:
                if char in self.lh_brace:
                    stack.append(char)
                elif char in self.rh_brace and len(stack) != 0:
                    temp = stack[-1] + char
                    if temp in self.brace_pairs:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            return not stack




