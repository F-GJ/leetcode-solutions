class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        read_ptr = 1
        write_ptr = 1
        while read_ptr < len(nums):
            if nums[read_ptr] == nums[write_ptr - 1]:
                read_ptr += 1
            else:
                nums[write_ptr] = nums[read_ptr]
                write_ptr += 1
                read_ptr += 1
        return write_ptr
