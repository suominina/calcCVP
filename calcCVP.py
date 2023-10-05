#! /usr/bin/env python3

import matplotlib.pyplot as plt


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

keys = ['VCR', 'BEP', 'MARGINAL_PROFIT', 'MARGINAL_PROFIT_RATIO', 'BEP_RATIO', \
        'MARGIN_OF_SAFETY_RATIO']
RES = []
ELEMENTS = input_elements()
revenue, variable, fixed = ELEMENTS


CVP = CVPAnalysis(revenue, variable, fixed)
RES.append(CVP.calc_vcr())
RES.append(CVP.calc_bep())
RES.append(CVP.calc_marginal_profit())
RES.append(CVP.calc_marginal_profit_ratio())
RES.append(CVP.calc_bep_ratio())
RES.append(CVP.calc_margin_of_safety_ratio())

#making format
WIDTH = 50
NUMBER_WIDTH = 10
ITEM_WIDTH = 37

FMT = '{{:{}}}{{:>{}.2f}}'.format(ITEM_WIDTH, NUMBER_WIDTH)

#show results
print('=' * WIDTH)

for i in range(len(RES)):
    print(FMT.format(keys[i], RES[i]))

print('=' * WIDTH)

#show graph
rLine = [0, revenue]
vLine = [fixed, fixed + variable]
fLine = [fixed, fixed]

plt.plot(rLine)
plt.plot(vLine)
plt.plot(fLine)

#delete axes
plt.xticks([])
plt.yticks([])

plt.show()