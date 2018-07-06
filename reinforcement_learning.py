#het reinforcement learning algoritme
import random

class reinforcement_player:    

    def __init__(self, game_matrix, player):
        self.game_matrix = game_matrix
        self.game_size = len(game_matrix)
        self.bitworths = [1] * self.game_size #alle acties hebben aan het begin 1 opgebracht.
        self.player = player
    
    def best_move(self, my_history, opponent_history):
        r = random.randint(0,9)
        if r == 0:                #als exploreren doe dan een randomactie
            r2 =  random.randint(0, self.game_size - 1)
            return r2
        else:  #exploiteren
            #stop de actie(s) met de hoogste waardes in een lijst
            best_moves = []
            highest = -1
            for move, value in enumerate(self.bitworths):
                if value == highest:
                    best_moves.append(move)
                elif value > highest:
                    best_moves = [move]
                    highest = value
            return random.choice(best_moves) #kies een van de acties met de hoogste waarde
    

    #tel de opbrengst van de laatst gedane zet op bij het totaal van wat de laatst gedane zet heeft opgebracht    
    def update(self, my_history, opponent_history):
        if self.player == 0:
            self.bitworths[my_history[-1]] += self.game_matrix[my_history[-1]][opponent_history[-1]]
        else:
            self.bitworths[my_history[-1]] += self.game_matrix[opponent_history[-1]][my_history[-1]]

