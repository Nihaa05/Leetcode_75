class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False

        n = len(nums)
        low, mid = float("inf"),float("inf")

        for i in range(n):
            if nums[i] > mid:
                return True

            if nums[i]<low:
                low= nums[i]
            elif nums[i] > low and nums[i]<mid:
                mid = nums[i]

        return False
