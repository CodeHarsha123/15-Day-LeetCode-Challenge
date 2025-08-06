class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        current_sum = 0 
        prevSum = {0:1}
        for n in nums:
            current_sum+=n 
            diff = current_sum-k
            res+=prevSum.get(diff,0)
            prevSum[current_sum]=1+prevSum.get(current_sum,0)
        return res