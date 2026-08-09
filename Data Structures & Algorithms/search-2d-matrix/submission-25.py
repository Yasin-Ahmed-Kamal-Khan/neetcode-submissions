class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        correctRow = None
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            middle = (top + bottom) // 2
            if matrix[middle][-1] < target:
                top = middle + 1
            elif matrix[middle][0] > target:
                bottom = middle - 1
            elif matrix[middle][0] <= target and matrix[middle][-1] >= target:
                correctRow = matrix[middle]
                break
            else:
                return False
        
        if correctRow is None:
            return False


        left = 0
        right = len(correctRow) - 1
        while left <= right:
            middle = (left + right) // 2
            if correctRow[middle] < target:
                left = middle + 1
            elif correctRow[middle] > target:
                right = middle - 1
            elif correctRow[middle] == target:
                return True
        return False