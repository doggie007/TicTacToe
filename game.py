
from players import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer

class TicTacToe:
    def __init__(self) -> None:
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
    
    @staticmethod
    def print_board_nums():
        for row in [[str(i) for i in range(j*3, j*3 + 3)] for j in range(3)]:
            print(f"|{'|'.join(row)}|")

    def print_board(self):
        for row in [self.board[i*3:i*3+3] for i in range(3)]:
            print(f"|{'|'.join(row)}|")
    
    def available_moves(self):
        return [i for i,spot in enumerate(self.board) if spot==' ']
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self,square,letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_index = square // 3
        row = self.board[row_index*3 : row_index*3 + 3]
        if all(spot == letter for spot in row):
            return True
        col_index = square % 3
        col = self.board[col_index::3]
        if all(spot == letter for spot in col):
            return True
        if square % 2 == 0:
            diagonal_1 = self.board[::4]
            diagonal_2 = self.board[2:8:2]
            if all(spot == letter for spot in diagonal_1) or all(spot == letter for spot in diagonal_2):
                return True
        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
    
    letter = 'X'

    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        if game.make_move(square, letter):
            if print_game:
                print(f"{letter} makes a move to square {square}")
                game.print_board()
                print('\n')
            if game.current_winner:
                if print_game:
                    print(f"{letter} wins")
                return letter
        letter = 'O' if letter == 'X' else 'X'
    if print_game:
        print("It's a tie")
        return "tie"

if __name__ == "__main__":
    x_player = HumanPlayer('X')
    o_player = SmartComputerPlayer('O')
    game = TicTacToe()
    play(game, x_player, o_player, print_game=False)