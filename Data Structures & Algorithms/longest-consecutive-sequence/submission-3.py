class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        ans = 0
        for num in numbers:
            if num-1 not in numbers:
                current_num = num
                length = 1
                while (current_num+1) in numbers:
                    length+=1
                    current_num +=1
                ans = max(ans,length)
        return ans