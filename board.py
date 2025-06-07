class Board:
    
    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.board_size = len(self.board)
    
    def print_board(self):
        '''prints the current board in the terminal'''
        print()
        for i in range(self.board_size):
            print(f"{self.board[i][0]}|{self.board[i][1]}|{self.board[i][2]}")
    
            if i < self.board_size-1:
                print("-+-+-")
        print()
            
#testing
tabuleiro = Board()

tabuleiro.print_board()
           