class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        maxconteur = 0
        for i in numset:
            if i-1 not in numset:
                a = i+1
                while a in numset :
                    a+=1
                maxconteur=max(a-i,maxconteur)
        return maxconteur