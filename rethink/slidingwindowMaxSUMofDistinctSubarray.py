from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        window_sum = 0
        max_sum = 0

        # First window
        for i in range(k):
            window_sum += nums[i]
            freq[nums[i]] += 1

        if len(freq) == k:
            max_sum = window_sum

        # Slide the window
        for i in range(k, len(nums)):
            left = nums[i-k]

            window_sum -= left
            freq[left] -= 1

            if freq[left] == 0:
                del freq[left]

            window_sum += nums[i]
            freq[nums[i]] += 1

            if len(freq) == k:
                max_sum = max(max_sum, window_sum)

        return max_sum
