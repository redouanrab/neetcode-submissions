class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft=[height[0]]
        maxright=[height[len(height)-1]]*len(height)
        water=0
        for i in range(1,len(height)):
            if height[i]>maxleft[i-1]:
                maxleft.append(height[i])
            else : 
                maxleft.append(maxleft[i-1])
        for i in range(len(height)-2,-1,-1):
            if height[i]>maxright[i+1]:
                maxright[i]=height[i]
            else : 
                maxright[i]=maxright[i+1]
        for i in range(len(height)):
            trappedwater=min(maxleft[i],maxright[i])-height[i]
            if trappedwater >=0:
                water+=trappedwater
        return water