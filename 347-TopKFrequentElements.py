class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counter = {}
        for n in nums:
            counter[n] = 1 + counter.get(n, 0) #iterates through list to count frequency of number "n" in list

        for key, val in counter.items():
            heapq.heappush(heap, (-val, key)) #simulating a max heap by making val negative 
        
        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        
        return res