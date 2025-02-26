class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # want to convert to a set for 0(1) lookups - efficient
        allowed = set(allowed)
        count = 0
        
        for word in words:
            is_consistent = True
            for characters in word:
                if characters not in allowed:
                    is_consistent = False
                    break
            if is_consistent:
                count += 1
        return count

        #Python specific function: all()
        """
        for word in words:
            if all(character in allowed for character in word):
                count +=1
        return count
        """