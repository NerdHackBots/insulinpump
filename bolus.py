#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 07:44:38 2019

@author: NerdHackBots
"""

#analysis
class insulin(object):
    bolus = 0
    
    def __init__(self, name, sugar_optimal, correction_factor, carb_ratio, insulin_on_board):
        self.name = name
        self.sugar_optimal = sugar_optimal
        self.correction_factor = correction_factor
        self.carb_ratio = carb_ratio
        self.insulin_on_board = insulin_on_board
    
    '''
    def insulin_on_board():
        pass
    '''
    
    def correction_insulin(self, sugar_current):
        if sugar_current > self.sugar_optimal:
            insulin_correct = (sugar_current - self.sugar_optimal) / self.correction_factor
            if self.insulin_on_board > insulin_correct:
                insulin_correct = 0
            else:
                insulin_correct = insulin_correct - self.insulin_on_board
        else:
            insulin_correct = 0
        return insulin_correct
    
    def carb_insulin(self, carb_amount):
        insulin_bolus = self.carb_ratio * carb_amount
        return insulin_bolus
    
    def total_insulin(self):
        insulin_total = self.insulin_bolus + self.insulin_correct
        return insulin_total
    
    def deliver_insulin(self):
        while self.insulin_total != 0:
            print(self.insulin_total)
