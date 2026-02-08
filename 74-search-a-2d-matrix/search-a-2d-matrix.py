class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bottom = 0, ROWS-1
        while top <= bottom:
            row = (top+bottom)//2
            if target < matrix[row][0]:
                bottom = row - 1 
            elif target > matrix[row][-1]:
                top = row + 1 
            else: 
                break #target is neither great than or less than the 0th or -1th point, lies in this row only! we found the row!

        l,r = 0, COLS-1
        while l <= r: 
            mid = (l+r)//2
            if target < matrix[row][mid]:
                r = mid - 1 
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                return True
        return False

#This is for the condition where we used to generally return -1 after the row is not found. 
        if not (top <= bottom):
            return False 
        


                
