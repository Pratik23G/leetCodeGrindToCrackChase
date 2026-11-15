class Solution:
    def reverseStrings(self, s: list[str]) -> None:
        def reverse(left: int, right: int):
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        reverse(0, len(s) - 1)
        start = 0
        end = 0

        for end in range(len(s) + 1):
            if end == len(s) or s[end] == " ":
                reverse(start, end - 1)
                start = end + 1

extestCase = ["I", " ", "a", "m", " ", "P"]

finalReverse = Solution()
finalReverse.reverseStrings(extestCase)
print(extestCase)