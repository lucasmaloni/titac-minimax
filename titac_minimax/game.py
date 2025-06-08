from board import Board
import copy

class Game:
    
    def __init__(self):
        self.board = Board()
        self.current_player = "X"
        
    def run(self):
        '''the main structure of the game and it's turn based logic'''
        while True:
            
            if self.current_player == "X":
                print(f'Player X, it is your turn!\nPlease inform the row and column to play:\n')
                self.board.print_board()
                
                while True: #player input loop
                    row = int(input("row: "))-1
                    column = int(input("column: "))-1
                    
                    if self.board.set_letter(self.current_player, row, column):
                        print(f'The decision was made, player X!\n') #end of the turn
                        break
                    else:
                        print('This play is not valid, pick a new one:')
            
            if self.current_player == "O":
                #the machine logic will enter here - further implementation required!
                print("now the machine must play")
                break
               
            self.board.print_board()
            
            if self.board.check_win(self.current_player):
                print(f'{self.current_player} won !')
                break
            
            if self.board.check_draw():
                print(f"it's a tie!")
                break
            
            self.change_player()
    
    def change_player(self):
        '''change current player based on current player'''
        if self.current_player == "X":
            self.current_player = "O"
            return
        
        if self.current_player == "O":
            self.current_player = "X"
            return    
    
    def evaluate(self, board):
        '''evaluates and return the current state of the game'''
        if board.check_win("X"): #human victory
            return -10
        elif board.check_win("O"): #machine victory
            return 10
        
        if board.check_draw():
            return 0

        return

    def copy_board(self, board): #provisory
        '''we copy the board Object for further use in the minimax'''
        board_copy = copy.deepcopy(board)
        return board_copy

    def minimax(self, board: Board, max_player: bool):
        ''''''
        
        if board.terminal():
            return self.evaluate(board)

        if max_player:
            '''machine scenario'''
            max_score = -float('inf')
            for move in board.get_possible_moves():
                board_copy = self.copy_board(board)
                board_copy.set_letter("O", *move)
                max_score = max(max_score, self.minimax(board_copy, False))
            return max_score

        if not max_player:
            '''human scenario'''
            min_score = float('inf')
            for move in board.get_possible_moves():
                board_copy = self.copy_board(board)
                board_copy.set_letter("X", *move)
                min_score = min(min_score, self.minimax(board_copy, True))
            return min_score
