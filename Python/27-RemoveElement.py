class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0   #index
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j

#test case
#solution = Solution()
#nums = [3,2,2,3]
#result = removeElement(nums, val)
#print(result)