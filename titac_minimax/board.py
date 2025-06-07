class Board:
    
    def __init__(self):
        self.EMPTY_SPACE = '     ' #5 SPACEBAR
        self.board = [[self.EMPTY_SPACE for i in range(3)] for i in range(3)] 
    
    def print_board(self):
        '''prints the current board in the terminal'''
        print()
        for i in range(3):
            print(f"{self.board[i][0]}|{self.board[i][1]}|{self.board[i][2]}")
    
            if i < 2:
                print("-----+-----+-----")
        print()
    
    def check_tile(self, row, column):
        '''returns boolean value if the picked tile is empty'''
        return self.board[row-1][column-1] == self.EMPTY_SPACE
    
    def set_letter(self, letter, row, column):
        '''assigns the X or O to the informed tile'''
        
        while not self.check_tile(row, column):
            print("can't place in this tile, choose another spot!")
            row = int(input("choose the row: "))
            column = int(input("choose the new column: "))
        
        #we format the letter assigned to not break the board format
        letter = "  "+letter+"  "
        self.board[row-1][column-1] = letter
  
#testing
tabuleiro = Board()

tabuleiro.print_board()

tabuleiro.set_letter("X", 1, 1)
tabuleiro.set_letter("O", 1, 2)
tabuleiro.set_letter("X", 1, 3)
tabuleiro.set_letter("O", 2, 1)
tabuleiro.set_letter("X", 2, 2)
tabuleiro.set_letter("O", 2, 3)
tabuleiro.set_letter("X", 3, 1)
tabuleiro.set_letter("O", 3, 2)
tabuleiro.set_letter("X", 3, 3)

tabuleiro.print_board()