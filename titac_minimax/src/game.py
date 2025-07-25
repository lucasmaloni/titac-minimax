from entities.board import Board
from entities.node import Node
from src.plotter import Plotter
import copy

class Game:
    
    def __init__(self):
        self.board = Board()
        self.current_player = "X"
        self.plotter = Plotter()
        self.round = 1
        
    def run(self):
        '''the main structure of the game and it's turn based logic'''
        while True:
            print(f'Round nº:{self.round}\n')
            
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
                self.board.set_letter("O", *best_move)
                print('the machine have played!')
            
                if self.round >= 5:
                    self.plotter.plot_tree(root_node) #plots current tree
            
            self.board.print_board()
            
            if self.board.check_win(self.current_player):
                print(f'{self.current_player} won !')
                break
            
            if self.board.check_draw():
                print(f"it's a tie!")
                break
            
            self.change_player()
            self.round += 1
    
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
        if board.check_win("X"): #human victory - min player
            return -10
        
        elif board.check_win("O"): #machine victory - max player
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
            board_copy = copy.deepcopy(board)   #we create a copy of the board
            board_copy.set_letter("O", *move)   #make the move in this parallel board
            score, child_node = self.minimax(board_copy, False) #call minimax to recursively evaluate this move
            child_node.move = move
            root_node.children.append(child_node)
            if score > max_score: #if the minimax score is bigger than the max score
                max_score = score   #we change the current max score for the biggre one
                best_move = move    #we change the best move - expecting the MAX result
        
        #returns a tuple that indicates the best position to be played
        root_node.score = max_score
        root_node.move = best_move
        return best_move, root_node
