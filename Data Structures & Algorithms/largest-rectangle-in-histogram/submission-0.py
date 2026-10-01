class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []
        n = len(heights)
        for i in range(len(heights)+1):
            cur = 0 if i == n else heights[i] 
            while stack and heights[stack[-1]]>=cur:
                height = heights[stack[-1]]
                stack.pop()
                left = stack[-1] if stack else -1
                width = (i - left-1)
                ans = max(ans, width*height)
            stack.append(i)
            
        return ans