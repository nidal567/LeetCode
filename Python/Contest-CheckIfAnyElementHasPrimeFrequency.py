class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for count in freq.values():
            if count < 2:
                continue
            for i in range(2, int(count**0.5) + 1):
                if count % i == 0:
                    break
            else:
                return True
        return False