
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        commonDict = {}
        

print(Solution().longestCommonSubsequence("abcde", "ace"))


def longestCommonSubsequence(self, text1, text2):
	l1, l2 = len(text1), len(text2)
	dp = [0]*(l2+1)
	for i in range(l1):
		cache = dp[0]
		for j in range(l2):
			cache, dp[j+1] = dp[j+1], cache + 1 if text1[i] == text2[j] else max(dp[j], dp[j+1])
	return dp[l2]
##https://leetcode.com/problems/longest-common-subsequence/discuss/598294/Python-and-C%2B%2B-DP-Rolling-(1D-array)-solution




class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]
        
        text1 = " " + text1
        text2 = " " + text2
        
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
        return dp[-1][-1]
##https://leetcode.com/problems/longest-common-subsequence/discuss/598285/Python-faster-than-90



from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @lru_cache(maxsize=None) # This memoize the function calls with arguments and returned results so that you can call again later on with same parameters without incurring additional computation. Max_size specifies that our LRU cache can grow without bounds.
        def memo_solve(ptr1, ptr2):
            if ptr1 == len(text1) or ptr2 == len(text2):
                return 0
            
            # Case 1
            if text1[ptr1] == text2[ptr2]:
                return 1 + memo_solve(ptr1+1, ptr2+1)
        
            # Case 2
            else:
                return max(memo_solve(ptr1+1, ptr2), memo_solve(ptr1,ptr2+1))
                            # ^ Case 2 - Option 1           ^ Case 2 - Option 2
        return memo_solve(0,0) # Start the recursion stack from str1[0] and str2[0]
##https://leetcode.com/problems/longest-common-subsequence/discuss/598508/Python-DP-solution-with-Explanation-%2B-Thinking-process-%2B-Diagram


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # padding one space for empty string representation
        text1 = ' ' + text1
        text2 = ' ' + text2

        w, h = len(text1), len(text2)

        dp_table = [ [ 0 for x in range(w) ] for y in range(h) ]

        # update dynamic programming table with optimal substructure
        for y in range(1, h):
            for x in range(1, w):

                if text1[x] == text2[y]:
                    # with the same character
                    # extend the length of common subsequence
                    dp_table[y][x] = dp_table[y-1][x-1] + 1
                
                else:
                    # with different characters
                    # choose the optimal subsequence
                    dp_table[y][x] = max( dp_table[y-1][x], dp_table[y][x-1] )

        return dp_table[-1][-1]

##https://leetcode.com/problems/longest-common-subsequence/discuss/598687/Python-O(-m*n-)-dynamic-programming.-85%2B-w-Hint

