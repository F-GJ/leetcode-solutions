class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for n in range(len(nums)):

            if nums[n] <= first:
                first = nums[n]

            elif nums[n] <= second and nums[n] > first:
                second = nums[n]

            else:
                return True
        return False
        