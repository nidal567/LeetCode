from math import gcd

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        output = []

        for denominator in range(2, n + 1):
            for numerator in range(1, denominator):
                if gcd(numerator, denominator) == 1:
                    output.append(f"{numerator}/{denominator}")
        return output