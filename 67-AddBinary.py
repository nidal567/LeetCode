class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

        #step by step
        #a_int, b_int = int(a, 2), int(b, 2) #binary string into integer of base 2
        #sum = a_int + b_int #sum the integers together
        #return bin(sum)[2:] #returns the integer sum into a binary (the [2:] takes off "0b")