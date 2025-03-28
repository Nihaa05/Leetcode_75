class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_w = 0
        num_zeros = 0
        n = len(nums)
        left = 0

        for right in range(n):
            if nums[right] == 0:
                num_zeros += 1

            while num_zeros > k:
                if nums[left] == 0:
                    num_zeros -= 1
                left += 1

            w = right - left + 1
            max_w = max(max_w , w)
        return max_w
