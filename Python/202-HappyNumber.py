class Solution:
    def isHappy(self, n: int) -> bool:
        number = set()

        while n != 1 and n not in number:
            number.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        
        return n == 1