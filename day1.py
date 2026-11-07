class Solution:
    def moveZeros(self, nums: list[int]) -> None:
        # we use 2 pointer technique to solve this problem
        left = 0
        right = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]

                left += 1

moveSol = Solution()
numArr = [1, 0, 2, 0, 12, 0, 13]
moveSol.moveZeros(numArr)
print(numArr)