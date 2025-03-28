class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_length = 0
        left = 0
        zero_count = 0

        for right in range(len(nums)):
            # Count zeros in the current window
            if nums[right] == 0:
                zero_count += 1
      
            # Shrink window from the left if more than one zero
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            
            # Calculate max length after deleting one element
            # If there's at least one zero in the window, we can delete it
            # If there are no zeros, we must delete one '1'
            current_length = right-left
            max_length = max(max_length, current_length)

        return max_length
