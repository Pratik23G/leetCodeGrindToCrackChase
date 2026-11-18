#today i solved a 3SumClosest problem in leetcode using two pointers and sorting technique

class Solution:
    def closest3Sum(self, nums:list[int], target: int) -> int:

        nums.sort()
        closeSum = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                currSum = nums[i] + nums[left] + nums[right]
                if abs(target - currSum) < abs(target - closeSum):
                    closeSum = currSum
                if currSum == target:
                    return currSum
                elif currSum < target:
                    left += 1
                else:
                    right -= 1

        return closeSum

exArr = [-1,2,1,3]
target = 1

finalCheck = Solution()

print(finalCheck.closest3Sum(exArr, target=1))