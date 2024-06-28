class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # My solution - check the sorted string, if it is not equal,
        # then it is not an anagram. We don't need the base case either
        if ''.join(sorted(s)) != ''.join(sorted(t)):
            return False
        else: 
            return True

#tester example
solution = Solution()
s = "danil"
t = "nidal"
result = solution.isAnagram(s, t)
print(result)