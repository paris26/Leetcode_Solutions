class Solution:
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        
        # Get lexicographically smallest and largest strings
        s1, s2 = min(strs), max(strs)
        
        # Find common prefix between these two
        for i, c in enumerate(s1):
            if i >= len(s2) or s2[i] != c:
                return s1[:i]
        return s1