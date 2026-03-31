class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        def sift_down(idx, heap_size, nums):
            while True:
                left = idx * 2 + 1
                right = idx * 2 + 2
                largest = idx
                if left < heap_size and nums[left] > nums[largest]:
                    largest = left

                if right < heap_size and nums[right] > nums[largest]:
                    largest = right 

                if nums[idx] == nums[largest]:
                    break

                nums[largest], nums[idx] = nums[idx], nums[largest]
                idx = largest

        for i in range((n//2)-1, -1, -1):
            sift_down(i, n, nums)

        for i in range(n-1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            sift_down(0, i, nums)

        return nums    