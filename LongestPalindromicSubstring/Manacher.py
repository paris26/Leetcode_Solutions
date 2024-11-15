class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        if len(s) == 1:
            return s

        # Transform the string to handle both odd and even length palindromes
        t = "^#" + "#".join(s) + "#$"
        n = len(t)

        # Array to store the radius of the palindrome centered at each position
        P = [0] * n

        # Initialize the center and right boundary of the rightmost palindrome
        center = right = 0

        # Variables to track the longest palindrome found
        max_center = max_len = 0

        for i in range(1, n - 1):
            if i < right:
                mirror = 2 * center - i
                P[i] = min(right - i, P[mirror])

            # Attempt to expand the palindrome centered at i
            while t[i + P[i] + 1] == t[i - P[i] - 1]:
                P[i] += 1

            if i + P[i] > right:
                center = i
                right = i + P[i]

            # Update the longest palindrome found so far
            if P[i] > max_len:
                max_len = P[i]
                max_center = i

        # Extract the start position in the original string
        start = (max_center - max_len) // 2
        return s[start : start + max_len]
