class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # MY SOLUTION - check the sorted string, if it is not equal,
        # then it is not an anagram. We don't need the base case either
        return ''.join(sorted(s)) == ''.join(sorted(t))
    
        #leetcode style, with algorithm
        #base case: check lengths
        if len(s) != len(t):
            return False
        
        counter = {}

        for char in s:
            counter[char] = counter.get(char, 0) + 1
        
        for char in t:
            if char not in counter or counter[char] == 0:
                return False
            counter[char] -= 1
        
        return True

#tester example
solution = Solution()
s = "danil"
t = "nidal"
result = solution.isAnagram(s, t)
print(result)