def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        slide and look through the array
        each window is length of k
        find average of each window
        check if the number is higher, if it is, store it in the return variable
        do not calculate each window, instead reuse the previous sum
        """

        first_win_sum = 0
        for i in range(k):
            first_win_sum += nums[i]
        max_avg = first_win_sum / (k * 1.0)
        i = 0
        while True:
            if i + k <= len(nums):
                win_sum = first_win_sum - nums[i] + nums[i+k]
                first_win_sum = win_sum
                max_avg = max(max_avg, win_sum / (k * 1.0))
            else:
                break
            i += 1
        return max_avg