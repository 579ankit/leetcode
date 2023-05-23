class Solution:
    def isValid(self, s: str) -> bool:
        my_d = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        l = []
        
        for i in s:
            if i in my_d.keys():
                l.append(i)
            elif len(l)==0 or i!=my_d[l.pop()]:
                return False
        return len(l)==0
      
