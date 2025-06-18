class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # want to count magazine
        freq_magazine = {}

        # count freq of each character in magazine
        for char in magazine:
            if char in freq_magazine:
                freq_magazine[char] += 1
            else:
                freq_magazine[char] = 1

        # now to check if ransomNote can be built
        for char in ransomNote:
            if char not in freq_magazine or freq_magazine[char] == 0:
                return False
            freq_magazine[char] -= 1

        return True