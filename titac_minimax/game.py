from board import Board

class Game:
    
    def __init__(self):
        self.board = Board()
        self.players = ['X', 'O']
        self.current_player = self.players[0]
        
    def run(self):
        '''the main structure of the game and it's turn based logic'''
        while True:
            print(f'Player {self.current_player}, it is your turn!\nPlease inform the row and column to play:\n')
            self.board.print_board()
            
            while True: #player input loop
                row = int(input("row: "))
                column = int(input("column: "))
                
                if self.board.set_letter(self.current_player, row, column):
                    print(f'The decision was made, player {self.current_player}!\n') #end of the turn
                    break
                else:
                    print('This play is not valid, pick a new one:')
                        
                    
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
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]     
    
    def evaluate(self):
        '''evaluates and return the current state of the game'''
        
        if self.board.check_win(self.players[0]):
            return -10
        elif self.board.check_win(self.players[1]):
            return 10
        
        if self.board.check_draw():
            return 0

        return

#testing
jogo = Game()

jogo.run()