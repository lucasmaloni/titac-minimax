from board import Board
from node import Node
from plotter import Plotter
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
                print("now the machine must play")
                best_move, root_node = self.find_best_move(self.board)
                plotter = Plotter()
                plotter.print_root_info(root_node)
                self.board.set_letter("O", *best_move)
                print('the machine have played!')
               
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

    def minimax(self, board: Board, max_player: bool):
        '''the minimax algorithm implemented'''
        if board.terminal():
            score = self.evaluate(board)
            terminal_node = Node(score) #at the end of the recursion, we assign a new and final node with a score to it
            return score, terminal_node

        if max_player:
            '''machine scenario'''
            max_score = -float('inf')
            
            #we create a new node, that have a list of nodes for every possible machine move in the moves list
            current_node = Node()
            for move in board.get_possible_moves():
                board_copy = copy.deepcopy(board)
                board_copy.set_letter("O", *move)
                minimax_value, child_node = self.minimax(board_copy, False)
                child_node.move = move
                current_node.children.append(child_node)
                max_score = max(max_score, minimax_value)
                
            current_node.score = max_score
            return max_score, current_node

        if not max_player:
            '''human scenario'''
            min_score = float('inf')
            
            #we create a new node, that have a list of nodes for every possible human move in the moves list
            current_node = Node()
            for move in board.get_possible_moves():
                board_copy = copy.deepcopy(board)
                board_copy.set_letter("X", *move)
                minimax_value, child_node = self.minimax(board_copy, True)
                child_node.move = move
                current_node.children.append(child_node)
                min_score = min(min_score, minimax_value)
            
            current_node.score = min_score
            return min_score, current_node
    
    def find_best_move(self, board: Board):
        '''finds the best move for the machine to play'''
        max_score = -float('inf')
        best_move = None
        root_node = Node()
        
        for move in board.get_possible_moves():
            board_copy = copy.deepcopy(board)
            board_copy.set_letter("O", *move)
            score, child_node = self.minimax(board_copy, False)
            child_node.move = move
            root_node.children.append(child_node)
            if score > max_score:
                max_score = score
                best_move = move
        
        #returns a tuple that indicates the best position to be played
        root_node.move = best_move
        return best_move, root_node

#testing
jogo = Game()
jogo.run()