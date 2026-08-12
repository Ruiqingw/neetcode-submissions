from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        candidates = deque()
        result = []

        for right,num in enumerate(nums):
            while candidates and nums[candidates[-1]]<num:
                candidates.pop()
            candidates.append(right)

            left = right-k+1
            while candidates[0]<left:
                candidates.popleft()
            if left>=0:
                result.append(nums[candidates[0]])
        return result