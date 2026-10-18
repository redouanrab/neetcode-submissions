class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefixe=[1]*n
        suffixe=[1]*n
        prefixe[0]=nums[0]
        suffixe[n-1]=nums[n-1]
        output=[1]*n
        for i in range(1,n):
            prefixe[i]=nums[i]*prefixe[i-1]
        for i in range(n-2,-1,-1):
            suffixe[i]=nums[i]*suffixe[i+1]
        for i in range(len(nums)):
            if i==0 :
                output[i]=suffixe[i+1]
            elif i==n-1:
                output[i]=prefixe[i-1]
            else :
                output[i]=suffixe[i+1]*prefixe[i-1]
        return output