class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign = 1
        res = 0
        idx = 0

        # Skip leading whitespace
        while idx < len(s) and s[idx] == " ":
            idx += 1

        # Check for the sign
        if idx < len(s) and (s[idx] == "-" or s[idx] == "+"):
            if s[idx] == "-":
                sign = -1
            idx += 1  # Move to the next character after the sign

        # Process numerical digits
        while idx < len(s) and "0" <= s[idx] <= "9":
            res = 10 * res + (ord(s[idx]) - ord("0"))
            idx += 1

            # Check for overflow/underflow
            if res > (2**31 - 1):
                return sign * (2**31 - 1) if sign == 1 else -(2**31)

        return res * sign
