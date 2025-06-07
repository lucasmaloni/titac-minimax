class Board:
    
    def __init__(self):
        self.EMPTY_SPACE = '     ' #5 SPACEBAR
        self.board_size = 3
        self.board = [[self.EMPTY_SPACE for i in range(self.board_size)] for i in range(self.board_size)]
    
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
        
        letter = "  "+letter+"  "
        self.board[row-1][column-1] = letter
    
    def check_win(self, letter):
        '''verifies all the win conditions'''
        letter = "  "+letter+"  "
        
        #checks for wins on the rows
        for i in range(self.board_size):
            row_verified = []
            for j in range(self.board_size):
                row_verified.append(self.board[i][j] == letter)
            
            if all(row_verified):
                return True, letter
        
        #checks for win on the columns
        for j in range(self.board_size):
            column_verified = []
            for i in range(self.board_size):
                column_verified.append(self.board[i][j] == letter)
            
            if all(column_verified):
                return True, letter
        
        #checks for diagonals win starting in the top left
        i = 0
        j = 0
        diagonal_verified = []
        while i < self.board_size:
            diagonal_verified.append(self.board[i][j] == letter)
            i += 1
            j += 1
            
        if all(diagonal_verified):
            return True

        diagonal_verified = []
        i = 0
        j = 2
        while i < self.board_size:
            diagonal_verified.append(self.board[i][j] == letter)
            i += 1
            j -= 1
        
        if all(diagonal_verified):
            return True
    
        
        
        
#testing
tabuleiro = Board()

tabuleiro.print_board()

tabuleiro.set_letter("O", 1, 1)
tabuleiro.set_letter("X", 1, 2)
tabuleiro.set_letter("X", 1, 3)
tabuleiro.set_letter("O", 2, 2)
tabuleiro.set_letter("X", 2, 1)
tabuleiro.set_letter("X", 2, 3)
tabuleiro.set_letter("X", 3, 1)
tabuleiro.set_letter("X", 3, 2)
tabuleiro.set_letter("O", 3, 3)

tabuleiro.print_board()
print(tabuleiro.check_win("O"))