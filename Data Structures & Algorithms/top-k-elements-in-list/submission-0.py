class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        for i in nums :
            if i not in dict:
                dict[i]=1
            else :
                dict[i]+=1
        L=[]
        for i in range(k):
            a=max(dict, key=dict.get)
            L.append(a)
            dict.pop(a)
        return L
