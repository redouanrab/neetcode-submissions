class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left= 0
        right = len(heights)-1
        water=0
        water=max(water,min(heights[left],heights[right])*(right-left))
        while left < right : 
            if heights[left]<heights[right]:
                left +=1
                water=max(water,min(heights[left],heights[right])*(right-left))
            elif heights[left]>heights[right]:
                right-=1
                water=max(water,min(heights[left],heights[right])*(right-left))
            elif heights[left] == heights[right] :
                left +=1
        return water