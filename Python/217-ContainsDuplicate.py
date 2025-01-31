class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        num_set = set()
        for i in nums:
            if i in num_set:
                return True
            num_set.add(i)
        return False
    
#test
solution = Solution()
nums = [1, 2, 4, 5, 1]
result = solution.containsDuplicate(nums)
print(result)