class Solution:
    def reverseWords(self, s: str) -> str:
        # Using python built-in
        """
        output = s.strip()
        output2 = output.split()
        output2.reverse()
        reverse = ' '.join(output2)
        return reverse
        """

        # Without using reverse built-in
        output = s.strip()
        output2 = output.split()

        # Indexes
        left = 0
        right = len(output2) - 1
        while left < right:
            # here we want to swap a tuple
            output2[left], output2[right] = output2[right], output2[left]
            # want to do this for all indices in list
            left += 1
            right -= 1
        result = ' '.join(output2)
        return result