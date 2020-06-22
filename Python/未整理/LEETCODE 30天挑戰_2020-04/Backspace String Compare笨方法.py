class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        real_S = ''
        real_T = ''
        for i in range(len(S)):
            if S[i] == '#':
                real_S = real_S[:-1]
            else:
                real_S += S[i]
        
        for i in range(len(T)):
            if T[i] == '#':
                real_T = real_T[:-1]
            else:
                real_T += T[i]
                
        if real_T == real_S:
            return True
        else:
            return False
