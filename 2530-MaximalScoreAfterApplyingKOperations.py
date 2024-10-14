class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # matrix = [[0 for _ in range(col)] for _ in range(row)]
        # Python by default does min-heap for heaps
        max_heap = [-1*i for i in nums] #multiplying every index in the 2D array by (-1)
        heapq.heapify(max_heap)
        output = 0
        
        for i in range(k):
            # pop max value from list as a positive number
            max_val = -heapq.heappop(max_heap)
            # add largest value to output
            output += max_val
            # ceil() rounds up to the next whole integer e.g. ceil(2.33) = 3
            heapq.heappush(max_heap, -ceil(max_val / 3))
            
        return output