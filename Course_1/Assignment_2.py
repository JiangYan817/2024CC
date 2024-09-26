##排序数组——归并排序
#给你一个整数数组 nums，请你将该数组升序排列。

#时间复杂度O(nlogn)


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums

        mid = len(nums) // 2
        lefthalf = nums[:mid]
        righthalf = nums[mid:]

        def merge(lefthalf, righthalf):
            result = []
            while lefthalf and righthalf:
                if lefthalf[0] < righthalf[0]:
                    result.append(lefthalf.pop(0))
                else:
                    result.append(righthalf.pop(0))

            while lefthalf:
                result.append(lefthalf.pop(0))

            while righthalf:
                result.append(righthalf.pop(0))

            return result

        return merge(self.sortArray(lefthalf), self.sortArray(righthalf))
