class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""

        ct,w={},{}
        for c in t:
            ct[c]=1+ct.get(c,0)
        have = 0
        need= len(ct)
        res=[-1,-1]
        reslen=float("infinity")
        l=0
        for r in range(len(s)):
            c=s[r]
            w[c]=1+w.get(c,0)

            if c in ct and w[c]==ct[c]:
                have+=1
            while have == need:
                if (r-l+1)<reslen:
                    reslen=r-l+1
                    res=[l,r]
                w[s[l]]-=1
                if s[l] in ct and w[s[l]]<ct[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if reslen!= float("infinity") else ""