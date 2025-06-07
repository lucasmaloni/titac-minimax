class Board:
    
    def __init__(self):
        self.EMPTY_SPACE = '    '
        self.board = [[self.EMPTY_SPACE for i in range(3)] for i in range(3)] 
    
    def print_board(self):
        '''prints the current board in the terminal'''
        print()
        for i in range(3):
            print(f"{self.board[i][0]}|{self.board[i][1]}|{self.board[i][2]}")
    
            if i < 2:
                print("----+----+----")
        print()
    
    def check_tile(self, row, column):
        '''returns boolean value if the picked tile is empty'''
        return self.board[row-1][column-1] == self.EMPTY_SPACE

            
#testing
tabuleiro = Board()

tabuleiro.print_board()
print(tabuleiro.check_tile(1, 1)) #true
           