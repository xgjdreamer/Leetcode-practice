class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=0
        substring=list()
        count=0
        
        for i in range(0, len(s)):
            newstring=''
            for t in range(i, len(s)):
                if t==i:
                    newstring=newstring+s[t]
                    substring.append(newstring)
                elif t>i and s[t]!=s[i]:
                    newstring=newstring+s[t]
                    substring.append(newstring)
                else:
                    break
        
        for x in substring:
            if duplicatestr(x) == 1:
                if len(x)>count:
                    count=len(x)
        
        if len(substring)==0:
            return 0
        else:
            return count
    
    
def duplicatestr(inpstr: str) -> int:
    lens=len(inpstr)
    listdup=list(inpstr)
    
    i=0
    flags=[0]*256

    while i<lens:
        if flags[ord(listdup[i])]==0:
            flags[ord(listdup[i])]+=1
            i=i+1
        else:
            return 0
    return 1
