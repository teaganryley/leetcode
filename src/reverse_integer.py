class ReverseInteger:
    """
    Assumptions:
        -input is "scrubbed". I assume that, because of decoupling, the theoretical interface will handle
        input validation, and therefore can expect integers
    """
    def solution1(self, num):
        solution = ''
        for i in str(abs(num)):
            solution = i + solution

        # simulate integer overflow
        if num.bit_length() < 32 and int(solution).bit_length() < 32 and num != 0:
            sign = num//abs(num)
            return int(solution) * sign
        else:
            return 0


if __name__ == "__main__":
    my_ri = ReverseInteger()
    solution = my_ri.solution1(123)
    print('Input: {0} | Output: {1} | Bit length: {2}'.format(123, solution, solution.bit_length()))
