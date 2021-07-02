import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self,game):
        spot = random.choice(game.available_moves())
        return spot

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid = False
        val = 0
        while not valid:
            square = input(f"{self.letter}'s turn. Input a move {{0-8}}:")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid = True
            except ValueError:
                print("Invalid square. Try again")
        return val

class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, state, player):

        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            return {'position': None, 'score': state.num_empty_squares() + 1 if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
        if not state.empty_squares():
            return {'position': None, 'score':0}


        if player == max_player:
            best_score = {'position':None, 'score': -math.inf}
        else:
            best_score = {'position':None, 'score': math.inf}

        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)

            state.board[possible_move] = ' '
            state.current_winner = None 
            sim_score['position'] = possible_move 
            if player == max_player:
                if sim_score['score'] > best_score['score']:
                    best_score = sim_score 
            else:
                if sim_score['score'] < best_score['score']:
                    best_score = sim_score 
        return best_score