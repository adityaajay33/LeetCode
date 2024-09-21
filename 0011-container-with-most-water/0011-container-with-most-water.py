class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        volume = (r-l)*min(height[r],height[l])

        while l<r:

            volume = max(volume, (r-l)*min(height[r],height[l]))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return volume
            
        