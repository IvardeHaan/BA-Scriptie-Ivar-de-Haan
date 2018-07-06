#gegeven 2 strategieen, geeft gemiddelde score van de rijspeler terug over een speelserie 

from __future__ import division
import markov_learner ,fictitious, reinforcement_learning

   
def player_vs_player(type1, type2, game_matrixA, game_matrixB):
    #maakt player_object aan
    if type1 == "markov":
        p1 = markov_learner.markov_player(game_matrixA, 0)    
    if type2 == "markov":
        p2 = markov_learner.markov_player(game_matrixB, 1)
    if type1 == "fictitious":
        p1 = fictitious.fictitious_player(game_matrixA, 0)
    if type2 == "fictitious":
        p2 = fictitious.fictitious_player(game_matrixB, 1)
    if type1 == "reinforcement":
        p1 = reinforcement_learning.reinforcement_player(game_matrixA,0)
    if type2 == "reinforcement":
        p2 = reinforcement_learning.reinforcement_player(game_matrixB,1)

    #initialiseer variabelen
    p1_history = []
    p2_history = []
    p1_total = 0
    rounds = 1000
    #speel games
    for k in range(rounds):
        p1_play = p1.best_move(p1_history,p2_history)
        p2_play = p2.best_move(p2_history,p1_history)
        p1_history.append(p1_play)
        p2_history.append(p2_play)
        p1.update(p1_history, p2_history)
        p2.update(p2_history, p1_history)
        p1_total += game_matrixA[p1_play][p2_play]
    return (p1_total / rounds)         #return gemiddelde score van player_1
    
    
    
