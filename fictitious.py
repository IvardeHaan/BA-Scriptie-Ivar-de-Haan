from __future__ import division
import random
class fictitious_player:
    def __init__(self, game_matrix, player):
        self.bitrates = {}
        self.player = player
        self.game_matrix = game_matrix
        self.game_size = len(game_matrix) 
        for k in range(self.game_size):   #iedere actie van de tegenstander is 0* gezien
            self.bitrates[k] = 0
            
    def update(self, your_history, opponent_history):
        self.bitrates[opponent_history[-1]] += 1 #tegenstander heeft zijn laatst gespeelde actie 1 keer meer gespeeld
            
    def best_move(self, my_history, opponent_history):
        total = 0
        probabilities = []
        for i in self.bitrates:              #stop de aantallen van gespeelde acties in een lijst, bereken totaal
            total += self.bitrates[i]
            probabilities.append(self.bitrates[i])      
        if total != 0:  #bereken kans van iedere actie
            probabilities = list(map(lambda x: x / total, probabilities))
        else:  #Als er nog geen acties zijn gespeeld, dan is iedere kans even zeker om gespeeld te worden
            probabilities = [0.5]*self.game_size
        moves_with_expec = []
        #bereken verwachte opbrengst voor iedere eigen actie
        for my_move in range(self.game_size):
            expec = sum([self.calc_expected_value(my_move, opponent_move, prob) for opponent_move, prob in enumerate(probabilities)])
            moves_with_expec.append(expec)
        best_moves = []
        highest = -1
        #stop de actie(s) met de hoogste waardes in een lijst
        for move, value in enumerate(moves_with_expec):
            if value == highest:
                best_moves.appen(move)
            elif value > highest:
                best_moves = [move]
                highest = value
        return random.choice(best_moves) #kies een van de acties met de hoogste waarde
    
    

        
    #bereken opbrengt van 2 zetten voor deze speler
    def calc_expected_value(self, my_move, opponent_move, prob):
        if self.player == 0:
            return self.game_matrix[my_move][opponent_move] * prob
        else:
            return self.game_matrix[opponent_move][my_move] * prob