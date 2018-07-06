#de markov-learner
from __future__ import division
import random
class markov_player:
    
    
    def __init__(self, game_matrix, player):
        self.bitrates = {}
        self.player = player
        self.game_matrix = game_matrix #dit is afhankelijk van wie jij speelt
        self.game_size = len(game_matrix)
        self.number_of_choices = []
        for k in range(self.game_size):
            self.number_of_choices += [0] 
            
    #voegt de nieuwe laatst geziene bitrate toe aan bitrates         
    def update(self, my_history, opponent_history):
        if len(my_history) >= 2:
            bits_history = tuple(zip(my_history[- 3: -1],  opponent_history[-3: -1]))

            if not bits_history in self.bitrates:
                self.bitrates[bits_history] = self.number_of_choices[:]
            self.bitrates[bits_history][opponent_history[-1]] += 1
        
        
    #geeft een beste zet terug gezien huidige verwachtingen
    def best_move(self, my_history, opponent_history, looking_forward = -1):
        #laatst geziene moves, kans(bij begin 1), utility bij verloop(bij begin 0)
        bit_history = [tuple(list(zip(my_history[-2:], opponent_history[-2:])) + [1, 0])] 
        #bereken alle paden hun verwachte kansen met de bithistory
        paths_with_expec_util = self.create_paths(2, bit_history)
        #geef beste zet terug, sommatie van waardes bij eigen acties hun bijbehorende paden
        return self.get_best_move(paths_with_expec_util)
    
    #bereken eerst waardes van ieder pad, dan sommaties, daarna beste zet
    def get_best_move(self, paths):
        expected_utils = [0]*self.game_size
        for path in paths:
            expected_utils[path[0][0]] += path[-2] * path[-1]
            
        best_moves = []
        highest = -1
        #stop de actie(s) met de hoogste waardes in een lijst
        for move, value in enumerate(expected_utils):
            if value == highest:
                best_moves.append(move)
            elif value > highest:
                best_moves = [move]
                highest = value
        return random.choice(best_moves) #kies een van de acties met de hoogste waarde
        
        
       
    #bereken recursive alle paden, en hun kansen
    def create_paths(self, length, paths):
         if length == 0:
             return paths
         else:
             new_paths = []
             for path in paths:
                 probs = self.calc_prob(path)
                 for my_move in range(self.game_size):
                     for opponent_move in range(self.game_size):
                         expected_value = self.calc_expected_value(probs, my_move, opponent_move)
                         new_paths.append(tuple(list(path[1:-2]) + [(my_move, opponent_move)] + [path[-2] * probs[opponent_move]] + [path[-1] + expected_value]))
                         #nieuwe pad met verwachte opbrengst
         return(self.create_paths(length - 1, new_paths))
                                
            

    #gegeven een bepaalde geschiedenis, berekent wat de tegenstander met welke 
    #waarschijnlijkheden gaat doen, geeft lijst  van kansen dat tegenstander zet doet
    def calc_prob(self, path):
        if not path[:-2] in self.bitrates:
            return [1 / self.game_size] * self.game_size
        else:
            
            bitrate = self.bitrates[path[:-2]]
            t = sum(bitrate)
            prob = []
            for k in range(self.game_size):
                prob.append(bitrate[k] / t)  
            return prob
        
    #berekent de opbrengst gegeven twee zetten voor deze speler
    def calc_expected_value(self, probability, my_move, opponent_move):
        if self.player == 0:
            return self.game_matrix[my_move][opponent_move] 
        else:
            return self.game_matrix[opponent_move][my_move]
  
    

        

        
        
        
        
    
            
