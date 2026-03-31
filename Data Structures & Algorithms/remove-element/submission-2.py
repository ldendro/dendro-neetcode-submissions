class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        valCounter = None
        for i, num in enumerate(nums):
            if num == val:
                if valCounter is None:
                    valCounter = i
            else:
                if valCounter is not None:
                    nums[valCounter], nums[i] = nums[i], nums[valCounter]
                    valCounter += 1
        return len(nums) if valCounter is None else valCounter 