#Main_ Doet experiment. Geeft gemiddeldes terug voor een groep onderling spelende strategieeen als rijspelers.

from __future__ import division


import speelserie

#instellen van gespeelde matrix
matrixA = [[3,0],[5,1]]
matrixB = [[3,5],[0,1]]

#instellen van spelende strategieen
strats = ["markov","reinforcement","fictitious"]



spelseries = 1000

total = 0

#iedere strategie speelt als rijspeler tegen iedere speelstrategie als kolomspeler
#return de gemiddelde waarde voor de rijspeler 
for player_a in strats:
    for player_b in strats:
        for k in range(spelseries):
            t = speelserie.player_vs_player(player_a, player_b, matrixA, matrixB)
            total += t
        print("rijspeler ", player_a, " vs ", player_b,": ", total / spelseries)
        total = 0




