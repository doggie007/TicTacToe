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
            square = input(f"{self.letter}'s turn. Input a move {{0-9}}:")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid = True
            except ValueError:
                print("Invalid square. Try again")
        return val