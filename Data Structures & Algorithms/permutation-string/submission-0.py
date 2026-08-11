class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        left = 0
        count1 = [0]*26
        # count2 = [0]*26
        for i in range(len(s1)):
            count1[ord(s1[i])-ord('a')]+=1
            count1[ord(s2[i])-ord('a')]-=1
            # count2[s2[i]]+=1
        if count1==[0]*26: 
            return True
        for right in range(len(s1),len(s2)):
            count1[ord(s2[right])-ord('a')]-=1
            count1[ord(s2[left])-ord('a')]+=1
            left+=1
            if count1==[0]*26:
                return True
        return False
            