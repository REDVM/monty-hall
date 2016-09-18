# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 12:35:58 2016

@author: red
"""


import numpy as np
import random

def play(choice, n_experience = 100000):
    win_count = 0
    doors = ["car", "goat", "goat"]
    for i in range(n_experience):
        random.shuffle(doors)
        
        # User choice #1
        chosen_door = random.randrange(3)
        
        showed_door = -1
        other_door = -1
        for i in range(len(doors)):
            if i != chosen_door:
                if doors[i] == "goat" and showed_door == -1:
                    showed_door = i
                else:
                    other_door = i
        
        # User choice #2
        if choice == "change":
            chosen_door = other_door
        else:
            chosen_door = chosen_door # Keep it
            
        if doors[chosen_door] == "car":
            win_count += 1
        
    return float(win_count) / n_experience


    
print "Probability to win in conserving the choice: ", play("conserve")
print "Probability to win in changing the choice: ", play("change")


