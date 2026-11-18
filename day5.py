#tody we are solving the longest palindromic substring problem 5

class Solution:
    def longestPalindromicSubs(self, s:str) -> str:
        resultStr = ""

        def solve(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]

        for i in range(len(s)):
            odd = solve(i, i)
            even = solve(i, i+1)

            resultStr = max(odd, even, resultStr, key=len)

        return resultStr

testStr = "ababd"

mainTest = Solution()

print(mainTest.longestPalindromicSubs(testStr))

print(testStr)
