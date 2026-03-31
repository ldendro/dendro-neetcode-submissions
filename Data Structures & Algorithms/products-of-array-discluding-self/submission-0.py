class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        leftRun = [1] * len(nums)
        for i in range(1, len(nums)):
            leftRun[i] = leftRun[i-1] * nums[i-1]

        rightRun = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            rightRun[i] = rightRun[i+1] * nums[i+1]

        for i in range(len(nums)):
            output[i] = leftRun[i] * rightRun[i]

        return output
