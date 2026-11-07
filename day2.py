# today we worked on understanding the duplicate zeros problem from Leetcode

class Solution:
    def duplicateZeros(self, nums:list[int]) -> None:

        countZeros = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                countZeros += 1

        readArr = len(nums) - 1
        writeArr = readArr + countZeros

        while readArr >= 0:
            print(f"Current readArr: {readArr}, writeArr: {writeArr}")
            if writeArr < len(nums):
                nums[writeArr] = nums[readArr]
                
            if nums[readArr] == 0:
                writeArr -= 1
                if writeArr < len(nums):
                    nums[writeArr] = 0

            writeArr -= 1
            readArr -= 1

checkDuplicates = Solution()
arrNum = [1, 0, 2,3,0,4,5,0]
checkDuplicates.duplicateZeros(arrNum)
print(arrNum)
