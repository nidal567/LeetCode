class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        output = []
        for i in range(len(prices)):
            discount = 0
            for j in range(len(prices)):
                if j > i and prices[j] <= prices[i]:
                    discount = prices[j]
                    break
            output.append(prices[i] - discount)
        return output