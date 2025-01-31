class Solution:
    def minimumSteps(self, s: str) -> int:
        output, ans = 0, 0
        for num in s:
            if num == '1':
                output += 1  
            else: 
                ans += output
        return ans



"""
OLD ANSWER DID NOT WORK - TIME LIMIT EXCEEDED DUE TO POOR TIME COMPLEXITY

class Solution:
    def minimumSteps(self, s: str) -> int:
        output = 0
        #string to list because strings are immutable
        s = list(s)

        for i in range(1, len(s)):
            #tuple swap
            if s[i-1] == '1' and s[i] == '0':
                s[i-1], s[i] = '0', '1'  
                output += 1
        return output


Think about string to list
s = "110"
s_list = list(s) #['1', '1', '0']
s_list[0], s_list[1] = s_list[1], s_list[0] #['0', '1', '1']
# if required to print out back in string format:
s_modified = "".join(s_list) # "011"
"""