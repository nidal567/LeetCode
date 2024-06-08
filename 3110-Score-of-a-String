class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        ### iterate through string up to the 2nd last character
        for i in range(len(s)-1):
            difference = abs(ord(s[i]) - ord(s[i + 1]))
            score += difference
        return score
    
solution = Solution()
example = "nidal"
result = solution.scoreOfString(example)
print(result)