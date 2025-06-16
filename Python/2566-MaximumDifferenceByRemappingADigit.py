class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        
        # maximum
        for i in s: 
            if i != '9':
                max_value = s.replace(i, '9')
                break
            else: 
                max_value = s

        #minimum
        for i, ch in enumerate(s): 
            if i == '1':
                if ch != '1':
                    min_value = s.replace(ch, '1')
                    break
            else:
                if ch != '0': 
                    min_value = s.replace(ch, '0')
                    break
        else:
            min_value = s
        
        return int(max_value) - int(min_value)
        