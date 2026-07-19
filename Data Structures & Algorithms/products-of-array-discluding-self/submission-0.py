class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        left = [1]*l
        right = [1]*l
        temp = 1
        for i in range(1,l):
            temp *=nums[i-1]
            left[i] = temp

        temp = 1
        for i in range(l-2,-1,-1):
            temp *=nums[i+1]
            right[i] = temp
        ans = [1]*l
        for i in range(l):
            ans[i] = left[i]* right[i]
        return ans
            