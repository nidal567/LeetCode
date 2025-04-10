class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #one-liner for fun
        #return len(s.strip().split()[-1])
        
        #3-liner using .split()
        #s = s.strip()
        #words = s.split()
        #return len(words[-1])

        #using no built-in functions
        length = 0
        i = len(s) - 1

        #skip trailing spaces for the last word
        while i > 0 and s[i] == '':
            i -= 1

        #count the characters of the last word
        while i > 0 and s[i] != '':
            length += 1
            i -= 1
        
        return length