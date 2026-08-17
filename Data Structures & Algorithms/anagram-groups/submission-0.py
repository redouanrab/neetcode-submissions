class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        l=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        for word in strs:
            cunt =[0]*26
            for c in word :
                idx = l.index(c)
                cunt[idx]+=1
            key = tuple(cunt)
            if key in dict.keys():
                dict[key].append(word)
            else : 
                dict[key]=[word]
        return list(dict.values())


            
