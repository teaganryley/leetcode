class ValidParentheses:
    """

    """
    def solution1(self, my_string):

        paren1 = {'(', ')'}
        paren2 = {'[', ']'}
        paren3 = {'{', '}'}

        lh_brace = {'(', '[', '}'}
        rh_brace = {')', ']', '}'}

        brace_pairs = {'()', '[]', '{}'}

        stack = []

        if len(my_string) % 2 == 1:
            return False
        elif my_string == '':
            return True
        else:
            for char in my_string:
                if char in lh_brace:
                    stack.append(char)
                elif char in rh_brace:
                    temp = char + stack[-1]

                    if temp in brace_pairs:
                        stack.pop()
                    else:
                        return False
                else:
                    return False


