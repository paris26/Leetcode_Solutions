import re


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Use regex to quickly identify the numeric substring with optional leading sign
        match = re.match(r"^[\s]*([+-]?\d+)", s)
        if not match:
            return 0  # Return 0 if no valid conversion

        # Convert the matched numeric substring to an integer directly
        num_str = match.group(1)
        result = int(num_str)

        # Clamp result to 32-bit integer bounds
        if result < -(2**31):
            return -(2**31)
        elif result > 2**31 - 1:
            return 2**31 - 1

        return result
