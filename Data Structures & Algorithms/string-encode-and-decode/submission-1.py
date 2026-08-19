class Solution:

    def encode(self, strs: List[str]) -> str:
        phrase=""
        for word in strs:
            n=len(word)
            phrase+=str(n)+"#"+word
        return phrase
    def decode(self, s: str) -> List[str]:
        l=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            n=int(s[i:j])
            word =s[j+1:j+1+n]
            l.append(word)
            i=j+n+1
        return l