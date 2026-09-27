class Solution:
    def maxArea(self, height: list[int]) -> int:
        ptr_one = 0
        ptr_two = len(height) - 1
        max_area = 0

        while ptr_one < ptr_two:
            current_area = (ptr_two - ptr_one) * min(height[ptr_one], height[ptr_two])
            max_area = max(max_area, current_area)

            if height[ptr_one] < height[ptr_two]:
                ptr_one += 1
            else:
                ptr_two -= 1
        return max_area