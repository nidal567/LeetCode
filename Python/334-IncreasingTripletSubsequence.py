class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        # We want to represent the smallest and middle numbers of the triplet
        # Initialize to infinity
        smallest = 10**10 # Can also use float(inf) better but not universal for IDEs
        middle = 10**10 # Can also use float(inf) better but not universal for IDEs

        # Iterate over the list of numbers
        for i in nums:
            # If curr > middle, an increasing triplet exists
            if i > middle:
                return True
            
            # If curr <= smallest, update curr to be smallest
            if i <= smallest:
                smallest = i
            
            # Otherwise, if smallest < curr < middle, update middle number
            else:
                middle = i
            
        # If no increasing triplet is found
        return False

solution = Solution()
example = [3, 10, 5, 8, 9, 11, 15]
result = solution.increasingTriplet(example)
print(result)