class Solution:
    def isHappy(self, n: int) -> bool:
        number = set()

        while n != 1 and n not in number:
            number.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        
        return n == 1

"""
class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(num):
            total = 0
            while num > 0:
                digits = num % 10
                total += digits * digits
                num = num // 10
            return total
        
        seen = set()
        while n!= 0 and n not in seen:
            seen.add(n)
            n = next_num(n)
        return n == 1
"""