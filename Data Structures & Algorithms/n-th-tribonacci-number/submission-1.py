class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        zero, one, two = 0, 1, 1
        for i in range(3, n+1):
            tempTwo = two
            tempOne = one
            two += one + zero 
            one = tempTwo
            zero = tempOne

        return two 