class Solution:
    def interpret(self, command: str) -> str:
        res = ''
        i = 0
        
        while i < len(command):
            if command[i] == 'G':
                res += 'G'
                i += 1
            else:
                if command[i+1] == 'a':
                    res += 'al'
                    i += 4
                else:
                    res += 'o'
                    i += 2
        
        return res
