
class EightQueens:
    def __init__(self) -> None:
        self.board = [[0] * 8 for i in range(8)] 
        self.solution = 0

    def is_attacked(self, row, col):
        col_left = col - row
        col_right = col + row
        for i in range(row):
            if self.board[i][col] == 1:
                return True
            if col_left >= 0 and self.board[i][col_left] == 1:
                return True 
            if col_right < 8 and self.board[i][col_right] == 1:
                return True 
            col_left += 1
            col_right -= 1
        return False
    
    def find_solution(self, row):
        if row == 8:
            self.solution += 1
            self.print_board()
        else:
            for col in range(8):
                if not self.is_attacked(row, col):
                    self.board[row][col] = 1
                    self.find_solution(row + 1)
                    self.board[row][col] = 0

    def print_board(self):
        print("Solution:", self.solution)
        for row in self.board:
            print(row)


queens = EightQueens()
queens.find_solution(0)