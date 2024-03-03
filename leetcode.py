# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"

# Solution

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = sorted(s.lower())
        b = sorted(t.lower())

        if a != b:
            return False
        else:
            return True

solution1 = Solution()
print(solution1.isAnagram(s = "rat", t = "car"))
