##排序数组——快速排序
#给你一个整数数组 nums，请你将该数组升序排列。

#时间复杂度O(nlogn)


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(nums,left,right):
            flag=nums[(left+right)//2]
            i,j=left,right
            while i<=j:
                while nums[i]<flag: i+=1
                while nums[j]>flag: j-=1
                if i<=j:
                    nums[i],nums[j]=nums[j],nums[i]
                    i+=1
                    j-=1
            if i<right: quicksort(nums,i,right)
            if j>left:  quicksort(nums,left,j)
        quicksort(nums,0,len(nums)-1)
        return nums