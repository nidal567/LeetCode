class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #time complexity O(n^2)
        for x in range(len(nums)):
            for y in range(x + 1, len(nums)):
                if nums[x] + nums[y] == target: 
                    return [x, y]
        
        #try more efficient: hashmaps
        hashmap = {}
        for i in range(len(nums)):
            #current + x = target
            x = target - nums[i]
            if x in hashmap:
                return [i, hashmap[x]]
            hashmap[nums[i]] = i
        
solution = Solution()
nums = [3, 4, 7, 9, 12]
target = 16
result = solution.twoSum(nums, target)
print(result)

#output for first function: [1, 4] | time O(n^2), space O(1)
#output for second function: [3, 2] | time O(n), space O(n)