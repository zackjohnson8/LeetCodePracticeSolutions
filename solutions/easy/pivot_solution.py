from typing import List

def solution(nums: List[int]) -> int:
    left_sum = 0
    right_sum = sum(nums)

    for index in range(len(nums)):
        # else subtract index value from right and add to left
        right_sum = right_sum - nums[index]

        # if left sum is equal to right sum return index
        if left_sum == right_sum:
            return index

        left_sum = left_sum + nums[index]

    return -1
