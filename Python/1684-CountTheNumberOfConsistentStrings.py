class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # want to convert to a set for 0(1) lookups - efficient
        allowed = set(allowed)
        count = 0

        for word in words:
            if all(character in allowed for character in word):
                count += 1
        return count