#! /usr/bin/env python3

import matplotlib.pyplot as plt
import tkinter as tk

class CVPAnalysis(object):
    def __init__(self, revenue, variable, fixed):
        self.revenue = revenue
        self.variable = variable
        self.fixed = fixed
    
    def calc_vcr(self):
        """calculate variable cost ratio"""
        self.vcr = self.variable / self.revenue
        return self.vcr
    
    def calc_bep(self):
        """calculate brake even point"""
        self.bep = self.fixed / (1 - self.vcr)
        return self.bep
    
    def calc_marginal_profit(self):
        """calculate marginal profit"""
        self.marginal_profit = self.revenue - self.variable
        return self.marginal_profit
    
    def calc_marginal_profit_ratio(self):
        """caluclate marginal profit ratio"""
        self.marginal_profit_ratio = self.marginal_profit / self.revenue
        return self.marginal_profit_ratio

    def calc_bep_ratio(self):
        """calculate bep ratio"""
        self.bep_ratio = self.bep / self.revenue
        return self.bep_ratio

    def calc_margin_of_safety_ratio(self):
        """calculate margin of safety ratio"""
        self.margin_of_safety_ratio = 1 - self.bep_ratio
        return self.margin_of_safety_ratio


def input_elements():
    revenue = int(input('revenue : '))
    variable = int(input('variable : '))
    fixed = int(input('fixed : '))
    return revenue, variable, fixed

def main():
    keys = ['VCR', 'BEP', 'MARGINAL_PROFIT', 'MARGINAL_PROFIT_RATIO', 'BEP_RATIO', \
            'MARGIN_OF_SAFETY_RATIO']
    res = []
    elements = input_elements()
    revenue, variable, fixed = elements


    cvp = CVPAnalysis(revenue, variable, fixed) 
    res.append(cvp.calc_vcr())
    res.append(cvp.calc_bep())
    res.append(cvp.calc_marginal_profit())
    res.append(cvp.calc_marginal_profit_ratio())
    res.append(cvp.calc_bep_ratio())
    res.append(cvp.calc_margin_of_safety_ratio())

    #setting format
    width = 50
    number_width = 10
    item_width = 37

    fmt = '{{:{}}}{{:>{}.2f}}'.format(item_width, number_width)

    #show results
    print('=' * width)
    for i in range(len(res)):
        print(fmt.format(keys[i], res[i]))
    print('=' * width)

    #show graphs
    revenueline = [0, revenue]
    variableline = [fixed, fixed + variable]
    fixedline = [fixed, fixed]

    plt.plot(revenueline)
    plt.plot(variableline)
    plt.plot(fixedline)

    #delete axes
    plt.xticks([])
    plt.yticks([])

    plt.show()
    

if __name__ == '__main__': main()