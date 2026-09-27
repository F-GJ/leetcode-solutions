class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[write_index], nums[i] = nums[i], nums[write_index]
                write_index += 1