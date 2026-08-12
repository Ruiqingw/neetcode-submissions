class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        need = {}
        window = {}
        for c in t:
            need[c] = need.get(c,0)+1
        have = 0
        need_count = len(need)

        left =0
        res_left = 0
        res_len = float("inf")
        
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c,0)+1

            if c in need and window[c]==need[c]:
                have +=1
            
            while have == need_count:
                if right-left+1<res_len:
                    res_len = right-left+1
                    res_left = left
                
                char = s[left]
                window[char]-=1
                if char in need and window[char]<need[char]:
                    have-=1
                left+=1
                
        if res_len==float("inf"):
            return ""
                
        return s[res_left:res_left+res_len]

            