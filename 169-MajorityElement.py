class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hashmap
        counter = {}
        result, maxCount = 0, 0

        for i in nums:
            counter[i] = 1 + counter.get(i, 0)
            result = i if counter[i] > maxCount else result
            maxCount = max(counter[i], maxCount)
        return result

    # follow up
        