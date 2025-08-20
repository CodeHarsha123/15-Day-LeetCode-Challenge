class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        numbers = []
        zero = []
        for i in nums:
            if i!=0:
                numbers.append(i)
            else:
                zero.append(0)
        nums[:]= numbers+zero
        