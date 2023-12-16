# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 18:35:22 2023

@author: Tarmo
"""
import numpy as np

sim_length = 1000000
rng = np.random.default_rng()
randints1 = rng.integers(low=0, high=3, size=sim_length)
randints2 = rng.integers(low=0, high=3, size=sim_length)
randints3 = rng.integers(low=0, high=2, size=sim_length)
randints4 = rng.integers(low=0, high=2, size=sim_length)

switch_wins = 0
keep_wins = 0
keep_rounds = sim_length // 2
switch_rounds = sim_length - keep_rounds
for i in range(sim_length):
    # The first random number designates the location of the main prize
    prize_index = randints1[i]
    # The second random number designates the choice of the conpetitor
    choice_index = randints2[i]
    # The third random number decides if the lower or greater indexed free slot
    # is revealed in case of prize and choice being the same
    matchcase_reveal_greater = randints3[i]
    # The switch parameter tells whether the competitor switched their choice
    # The competitor switches in even iterations i and keeps in odd iterations
    switched = (i % 2 == 0)
    # List free_ix will consist of indices that the host could reveal.
    # Variable free shall be the index of the slot the host reveals.
    # Variable if_switch designates the index if the competitor switches
    free_ix = [0, 1, 2]
    free_ix.remove(prize_index)
    if prize_index != choice_index:
        free_ix.remove(choice_index)
    reveal_ix = free_ix[0]
    if_switch = prize_index
    if prize_index == choice_index:
        if_switch = free_ix[1]
        if matchcase_reveal_greater == 1:
            reveal_ix = free_ix[1]
            if_switch = free_ix[0]
    # Variable final_index designates the final slot the contestant chooses
    final_index = if_switch if switched else choice_index
    victory = 1 if final_index == prize_index else 0
    if switched:
        switch_wins += victory
    else:
        keep_wins += victory
print("Switch win percentage:", 100*switch_wins/switch_rounds, " %")
print("Keep win percentage:", 100*keep_wins/keep_rounds, " %")
