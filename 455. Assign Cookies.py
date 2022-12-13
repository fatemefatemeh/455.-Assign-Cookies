class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s=sorted(s)
        g=sorted(g)
        i,j=0,0
        while i<len(g) and j<len(s):
            if s[j]>=g[i]:
                i+=1
            j+=1
        return i