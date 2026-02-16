import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self):
        self.name = ''
        self.symbol = ''

    def choose_name(self):
        while True:
            name = input('Enter your name (letters only): ')
            if name.isalpha():
                self.name = name
                break
            print('Invalid input. Please use letters only.')
            
            
    def choose_symbol(self):
        while True:    
            symbol = input(f'{self.name}, choose your symbol (a single letter): ')
            if symbol.isalpha() and len(symbol) == 1 :
                self.symbol = symbol.upper()
                break
            print( 'Invalid input. Please enter a single letter.')

class Menu:
    def display_main_menu(self):      
        print('Welcome to Tic Tac Toc game!')
        print('Choose:-\n1) Start game.\n2) Quit game')
        choice = input("Enter your choice ( 1 or 2 ): ")
        while choice not in ('1', '2'):
            choice = input('Invalid input. Please enter (1 or 2) only: ')
        return choice
    
    def display_endgame_menu(self):
        print('Choose:-\n1) Restart game.\n2) Quit game')
        choice = input("Enter your choice ( 1 or 2 ): ")
        while choice not in ('1', '2'):
            choice = input('Invalid input. Please enter (1 or 2) only: ')
        return choice
    
class Board:
    def __init__(self):
        self.board = ['1','2', '3','4','5','6','7','8','9']

    def display_baord(self):       
        for i in range(0,9,3):
            print(f' | '.join(self.board[i:i+3]))
            if i < 6:
                print("-"*9)
        
    
    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice-1] = symbol
            clear_screen()
            return True
        else:
            return False

    def is_valid_move(self, choice):
        return self.board[choice-1].isdigit()

    def reset_board(self):
        self.board = ['1','2', '3','4','5','6','7','8','9']

class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    def start_game(self):
        clear_screen()
        choice = self.menu.display_main_menu()
        if choice == '1':
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        for num, player in enumerate(self.players):
            clear_screen()
            print(f'Player-{num+1}, Enter your details:-')
            player.choose_name()
            player.choose_symbol()
            
    def play_game(self):
        clear_screen()
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                if self.check_draw():
                    self.board.display_baord()
                    print('It is tie')
                    time.sleep(3)
                    clear_screen()
                
                else:
                    self.board.display_baord()
                    print(f'Congratulations!! {self.players[self.current_player_index - 1].name} win the game.')
                    time.sleep(3)
                    clear_screen()
                choice = self.menu.display_endgame_menu()
                if choice == '1':
                    self.restart_game()
                else:
                    self.quit_game()
                    break

    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_baord()
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice = int(input("Choose a cell (1-9): "))
                if 1 <= cell_choice <=9 and self.board.is_valid_move(cell_choice):
                    break
                else:
                    print('This number has already chosen. Choose a valible number')
            except ValueError:
                print('Please enter a number between 1 and 9')
        self.board.update_board(cell_choice,player.symbol)
        self.switch_player()

    def check_win(self):
        win_combinations = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for combo in win_combinations:
            if (self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]):
                return True
        return False
    
    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)
    
    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def restart_game(self):
        self.board.reset_board()
        clear_screen()
        self.current_player_index = 0
        self.play_game()

    def quit_game(self):
        print('Thank you for Playing')




game = Game()

game.start_game()
