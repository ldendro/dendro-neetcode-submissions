class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        globEven = globOdd = currEven = currOdd = 1
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                currEven = currOdd = 1
            elif i % 2 == 0:
                if arr[i-1] > arr[i]:
                    currEven += 1
                    currOdd = 1
                else:
                    currEven = 1
                    currOdd += 1
            else:
                if arr[i-1] > arr[i]:
                    currOdd += 1
                    currEven = 1
                else:
                    currEven += 1
                    currOdd = 1
            globEven = max(globEven, currEven)
            globOdd = max(globOdd, currOdd)

        return max(globEven, globOdd)