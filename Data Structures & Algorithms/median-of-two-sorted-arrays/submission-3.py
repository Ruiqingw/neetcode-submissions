class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1,nums2
        if len(nums1)>len(nums2):
            A, B = B, A
        m, n = len(A),len(B)
        total = m+n
        half = total//2
        ans = 0
        l, r = 0,m
        while l<=r:
            i = l+(r-l)//2
            j = half - i
            Aleft = A[i-1] if i > 0 else float("-inf")
            Aright = A[i] if i < m else float("inf")
            Bleft = B[j-1] if j > 0 else float("-inf")
            Bright = B[j] if  j < n else float("inf")
            if Aleft<=Bright and Aright>=Bleft:
                if total%2==0:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
                else:
                    return min(Aright,Bright)
            elif Aleft>Bright:
                l-=1
            elif Aright<Bleft:
                l+=1
                    
