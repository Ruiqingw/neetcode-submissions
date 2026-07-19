class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = len(nums)
        if k>l:
            return []
        fre = {}
        for num in nums:
            fre[num] = fre.get(num,0)+1
        bucket = [[]for _ in range(l+1)]
        for num,count in fre.items():
            bucket[count].append(num)
        result = []
        for i in range(l,0,-1):
            for num in bucket[i]:
                result.append(num)
            if len(result)==k:
                return result