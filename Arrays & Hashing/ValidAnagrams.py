class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # both strings should have the same length
        if len(s) != len(t):
            return False
        # sort the strings and compare
        return sorted(s) == sorted(t)
