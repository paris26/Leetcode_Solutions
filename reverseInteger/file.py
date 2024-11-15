class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negative = x < 0
        x = abs(x)

        reversed_num = 0
        while x != 0:
            digit = x % 10
            x = x // 10
            reversed_num = reversed_num * 10 + digit

        if reversed_num > 2**31 - 1:
            return 0

        return -reversed_num if is_negative else reversed_num
