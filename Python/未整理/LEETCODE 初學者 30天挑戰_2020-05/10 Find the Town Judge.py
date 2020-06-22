from typing import List

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        count = {}
        judge = set()
        for t in trust:
            if t[1] in count:
                count[t[1]] += 1
            else:
                count[t[1]] = 1
            judge.add(t[0])
        for c in count:
            if count[c] == N - 1:
                if c not in judge:
                    return c
                
        if len(trust) == 0 and N == 1:
            return 1
        return -1
        
print(Solution().findJudge(2, [[1,2]]))
print(Solution().findJudge(3, [[1,3],[2,3]]))
print(Solution().findJudge(3, [[1,3],[2,3],[3,1]]))
print(Solution().findJudge(3, [[1,2],[2,3]]))
print(Solution().findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))
print(Solution().findJudge(1, []))
print(Solution().findJudge(4, [[1,2],[3,2],[1,3],[4,1],[3,1],[2,1],[2,3],[4,3],[4,2],[3,4],[2,4]]))


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        count = [0] * (N + 1)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1   
        for i in range(1, N + 1):
            if count[i] == N - 1:
                return i
        return -1


class Solution:
    def findJudge(self, N: int, trust) -> int:
        if N == 1 and trust == []:
            return 1
        from collections import defaultdict
        d = defaultdict(int)

        for a, b in trust:
            d[b] += 1

        ans = []
        for key in d.keys():
            if d[key] == N - 1:
                ans.append(key)

        if len(ans) != 1:
            return -1
        else:
            for a, b in trust:
                if a == ans[0]:
                    return -1
            return ans[0]
