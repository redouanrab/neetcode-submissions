class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=[]
        nums=sorted(nums)
        i=0
        while i < len(nums)-2: 
            while nums[i] == nums[i-1] and 0<i<len(nums)-2 :
                i+=1
            left,right=i+1,len(nums)-1
            while left < right:
                s = -(nums[left]+nums[right])
                if nums[i] == s :
                    l.append([nums[i],nums[left],nums[right]])
                    right -=1
                    left+=1
                    while left<right and nums[left]==nums[left-1] : 
                        left+=1
                elif nums[i] < s : 
                    left +=1
                elif nums[i] > s :
                    right -= 1
            i+=1
        return l