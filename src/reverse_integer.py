class ReverseInteger:
    """
    Assumptions:
        -input is "scrubbed". I assume that, because of decoupling, the theoretical interface will handle
        input validation, and therefore can expect integers
    """
    def solution1(self, num):
        """

        :param num: int
        :return: int
        """
        solution = ''
        for i in str(num):
            print(i)
            solution = i + solution
        print(solution)


if __name__ == "__main__":
    my_ri = ReverseInteger()
    my_ri.solution1(123)
