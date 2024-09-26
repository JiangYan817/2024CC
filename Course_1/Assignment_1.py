## 二分查找
# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

#时间复杂度O(logn)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums)-1
        while first <= last:
            midpoint = (first + last) // 2
            if target < nums[midpoint]:
                last = midpoint - 1
            elif target > nums[midpoint]:
                first = midpoint +1
            else:
                return midpoint
        return -1