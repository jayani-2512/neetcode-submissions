class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] ==".":
                    continue
                if board[i][j] not in row:
                    row.add(board[i][j])
                else:
                    return False
        for j in range(9):
            col = set()
            for i in range(9):
                if board[i][j] ==".":
                    continue
                elif board[i][j] not in col:
                    col.add(board[i][j])
                else:
                    return False
        


        for row in range(0,9,3):
            for col in range(0,9,3):
                box=set()
                for i in range(row,row+3):
                    for j in range(col,col+3):
                        if board[i][j]==".":
                            continue
                        elif board[i][j] not in box:
                            box.add(board[i][j])
                        else:
                            return False
        return True

