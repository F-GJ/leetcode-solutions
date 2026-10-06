class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        read_ptr = 0
        write_ptr = 0

        while read_ptr < len(nums):
            if nums[read_ptr] == val:
                read_ptr += 1
            else:
                nums[write_ptr] = nums[read_ptr]
                write_ptr += 1
                read_ptr += 1
        return write_ptr
