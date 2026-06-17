class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.b_search(nums, 0, len(nums) - 1, target)

    def b_search(self, nums, start, end, target):
        if start > end:
            return -1

        mid = (start + end) // 2

        if nums[mid] == target:
            return mid

        if target < nums[mid]:
            return self.b_search(nums, start, mid - 1, target)
        else:
            return self.b_search(nums, mid + 1, end, target)