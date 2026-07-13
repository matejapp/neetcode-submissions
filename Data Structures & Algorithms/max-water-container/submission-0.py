from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Initialize two pointers at opposite ends
        left = 0
        right = len(heights) - 1
        max_water = 0
        
        # Meet in the middle
        while left < right:
            # Width is the horizontal distance between pointers
            width = right - left
            
            # Height is limited by the shorter of the two walls
            current_height = min(heights[left], heights[right])
            
            # Calculate current area and update maximum if it's larger
            current_area = current_height * width
            max_water = max(max_water, current_area)
            
            # Move the pointer pointing to the shorter wall inward
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        return max_water
