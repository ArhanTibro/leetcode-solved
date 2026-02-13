class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans=[]
        track={}
        n=len(s)
        i=0
        for j in range(9,n):
            temp=s[i:j+1]
            if temp in track:
                if temp not in ans:
                    ans.append(temp)
            else:
                track[temp]=True
            i+=1
        return ans