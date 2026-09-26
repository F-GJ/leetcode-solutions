class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = [1] * len(nums)
        left_product = 1
        right_product = 1

        for x in range(len(nums)):
            answer[x] = left_product
            left_product *= nums[x]
        
        for y in range(len(nums)-1, -1, -1):
            answer[y] *= right_product
            right_product *= nums[y]
        
        return answer