"""Simple class example with robots"""
import pandas as pd

class Robot():
    
    def __init__(self, power=None, legs=2, arms=7, moves=True):
        self.power = power
        self.legs = legs
        self.arms = arms
        self.moves = moves

    def Move(self):
        if self.moves:
            print("The robot is walking!")
        else:
            print("The robot is broken!")    
