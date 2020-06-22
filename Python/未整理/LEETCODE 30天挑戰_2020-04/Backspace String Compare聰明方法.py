class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        Sp = len(S) - 1
        Tp = len(T) - 1
        while Sp and Tp > 0:
            if S[Sp] == '#':
                print("S去#")
                if Sp-2 >= 0:
                    Sp -= 2
                    continue
            if T[Tp] == '#':
                print("T去#")
                if Tp -2 >= 0:
                    Tp -= 2    
                    continue
            if S[Sp] == T[Tp]:
                Sp -= 1
                Tp -= 1
            else:
                print(S[Sp], T[Tp])
                return False
        return True

print(Solution().backspaceCompare("aab#c","ad#c"))
