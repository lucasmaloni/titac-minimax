class Board:
    
    def __init__(self):
        self.EMPTY_SPACE = ' '
        self.board_size = 3
        self.board = [[self.EMPTY_SPACE for i in range(self.board_size)] for i in range(self.board_size)]
    
    def print_board(self):
        '''prints the current board in the terminal'''
        for i in range(3):
            print(f"  {self.board[i][0]}  |  {self.board[i][1]}  |  {self.board[i][2]}  ")
    
            if i < 2:
                print("-----+-----+-----")
        print()
    
    def check_tile(self, row, column):
        '''returns boolean value if the picked tile is empty'''
        return self.board[row-1][column-1] == self.EMPTY_SPACE
    
    def set_letter(self, letter, row, column):
        '''assigns the X or O to the informed tile'''
        if self.check_tile(row, column):
            self.board[row][column] = letter
            return True
        
        #in case the tile is already ocupied
        return False
    
    def check_win(self, letter):
        '''verifies all the win conditions'''
        #letter = "  "+letter+"  "
        
        #checks for wins on the rows
        for i in range(self.board_size):
            row_verified = []
            for j in range(self.board_size):
                row_verified.append(self.board[i][j] == letter)
            
            if all(row_verified):
                return True
        
        #checks for win on the columns
        for j in range(self.board_size):
            column_verified = []
            for i in range(self.board_size):
                column_verified.append(self.board[i][j] == letter)
            
            if all(column_verified):
                return True            
        
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

        #checks for diagonal starting from de top rightS
        diagonal_verified = []
        i = 0
        j = 2
        while i < self.board_size:
            diagonal_verified.append(self.board[i][j] == letter)
            i += 1
            j -= 1
        
        if all(diagonal_verified):
            return True

        return False #caso de não vitoria

    def check_draw(self):
            '''checks if the current board defines a tie'''
            for i in range(self.board_size):
                for j in range(self.board_size):
                    if self.board[i][j] == self.EMPTY_SPACE:
                        return False
            
            return True
     
    def get_possible_moves(self):
        '''returns the list of every possible combination of line and column to play'''
        possible_moves = []
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] == self.EMPTY_SPACE:
                    possible_moves.append((i, j))
        
        return possible_moves
    
    def terminal(self):
        return self.check_win("O") or self.check_win("X") or self.check_draw()