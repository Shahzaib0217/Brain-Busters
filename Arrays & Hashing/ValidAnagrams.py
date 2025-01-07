class Solution:
    # Solution 1
    def isAnagram(self, s: str, t: str) -> bool:
        # both strings should have the same length
        if len(s) != len(t):
            return False
        # sort the strings and compare
        return sorted(s) == sorted(t)
    
    # Solution 2
    def isAnagram(self, s: str, t: str) -> bool:
        # Both strings should have the same length
        if len(s) != len(t):
            return False
        
        # Step 1: Count the occurrences of each character in the first string
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # Step 2: Subtract the occurrences while traversing the second string
        for char in t:
            if char not in count:
                return False  # If a character is in `t` but not in `s`
            count[char] -= 1
            if count[char] < 0:
                return False  # If count becomes negative
        
        # Step 3: Ensure all counts are zero
        return all(value == 0 for value in count.values())
