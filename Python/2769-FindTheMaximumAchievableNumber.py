class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return (num + 2*t)
    
solution = Solution()
num, t = 3, 2
result = solution.theMaximumAchievableX(num, t)
print(result)
