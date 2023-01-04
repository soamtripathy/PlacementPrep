class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # count = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[i])):
        #         if grid[i][j] < 0:
        #             count += 1
        #         else:
        #             continue
        # return count
        row_len = len(grid[0])
        col_len = len(grid)
        
        i = 0 
        j = row_len - 1
        total = 0
        
        while i < col_len and j >= 0:
            if grid[i][j] < 0:
                total += col_len - i
                j -= 1
            else:
                i += 1
        return total