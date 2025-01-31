from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list) #mapping charCount to list of anagrams

        for s in strs:
            count = [0] * 26 # a ... z
            
            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()

#test
solution = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
result = solution.groupAnagrams(strs)
print(result)