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
    
    def append_results(self, res):
            res.append(round(self.calc_vcr(), 2))
            res.append(round(self.calc_bep(), 2))
            res.append(round(self.calc_marginal_profit(), 2))
            res.append(round(self.calc_marginal_profit_ratio(), 2))
            res.append(round(self.calc_bep_ratio(),2 ))
            res.append(round(self.calc_margin_of_safety_ratio(),2 ))

class Application(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.create_variables()
        self.create_widgets()
        self.create_layout()
        
    def create_variables(self):
        self.var1 = tk.StringVar(self.root)
        self.var2 = tk.StringVar(self.root)
        self.var3 = tk.StringVar(self.root)
        self.keys = ['VCR', 'BEP', 'MARGINAL_PROFIT', 'MARGINAL_PROFIT_RATIO', 'BEP_RATIO', \
                'MARGIN_OF_SAFETY_RATIO']
        self.res = []

    def create_widgets(self):
        #spinbox
        self.revenue_spinbox = tk.Spinbox(self.root, textvariable=self.var1, format="%0.2f")
        self.variable_spinbox = tk.Spinbox(self.root, textvariable=self.var2, format="%0.2f")
        self.fixed_spinbox = tk.Spinbox(self.root, textvariable=self.var3, format="%0.2f")
        self.revenue_spinbox['width'] = 15
        self.variable_spinbox['width'] = 15
        self.fixed_spinbox['width'] = 15

        #labels for spinbox
        self.spinbox_label1 = tk.Label(self.root, text="revenue")
        self.spinbox_label2 = tk.Label(self.root, text="variable")
        self.spinbox_label3 = tk.Label(self.root, text="fixed")

        #button to execute
        
        self.submit_btn = tk.Button(self.root)
        self.submit_btn['text'] = 'execute'
        self.submit_btn['command'] = self.create_graph

        #labels that display the results
        self.resultLabel1 = tk.Label(self.root)
        self.resultLabel2 = tk.Label(self.root)
        self.resultLabel3 = tk.Label(self.root)
        self.resultLabel4 = tk.Label(self.root)
        self.resultLabel5 = tk.Label(self.root)
        self.resultLabel6 = tk.Label(self.root)
        self.resultValueLabel1 = tk.Label(self.root)
        self.resultValueLabel2 = tk.Label(self.root)
        self.resultValueLabel3 = tk.Label(self.root)
        self.resultValueLabel4 = tk.Label(self.root)
        self.resultValueLabel5 = tk.Label(self.root)
        self.resultValueLabel6 = tk.Label(self.root)

    def create_layout(self):
        
        padWE = dict(sticky=(tk.W, tk.E), padx='0.5m', pady='0.5m')
        self.revenue_spinbox.grid(row=0, column=1, **padWE)
        self.variable_spinbox.grid(row=1, column=1, **padWE)
        self.fixed_spinbox.grid(row=2, column=1, **padWE)
        self.submit_btn.grid(row=3, column=1, **padWE)

        self.spinbox_label1.grid(row=0, column=0, sticky=tk.W)
        self.spinbox_label2.grid(row=1, column=0, sticky=tk.W)
        self.spinbox_label3.grid(row=2, column=0, sticky=tk.W)

        self.resultLabel1.grid(row=5, column=0, sticky=tk.W)
        self.resultLabel2.grid(row=6, column=0, sticky=tk.W)
        self.resultLabel3.grid(row=7, column=0, sticky=tk.W)
        self.resultLabel4.grid(row=8, column=0, sticky=tk.W)
        self.resultLabel5.grid(row=9, column=0, sticky=tk.W)
        self.resultLabel6.grid(row=10, column=0, sticky=tk.W)

        self.resultValueLabel1.grid(row=5, column=1, sticky=tk.E)
        self.resultValueLabel2.grid(row=6, column=1, sticky=tk.E)
        self.resultValueLabel3.grid(row=7, column=1, sticky=tk.E)
        self.resultValueLabel4.grid(row=8, column=1, sticky=tk.E)
        self.resultValueLabel5.grid(row=9, column=1, sticky=tk.E)
        self.resultValueLabel6.grid(row=10, column=1, sticky=tk.E)
        self.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.columnconfigure(0, weight=2)
        #self.root.grid_columnconfigure(1, weight=1)
        

    def convert_spinbox_to_float(self):
        """this method converts spinbox into float"""
        x = self.revenue_spinbox.get()
        y = self.variable_spinbox.get()
        z = self.fixed_spinbox.get()

        #these variables are given to CVPAnalysis
        self.revenue = float(x)
        self.variable = float(y)
        self.fixed = float(z)
        
    def calculate_elements(self):
        self.cvp = CVPAnalysis(self.revenue, self.variable, self.fixed) 
        self.res = []
        self.cvp.append_results(self.res)

        #arrange the calculated results to labels
        self.resultLabel1.config(text=self.keys[0])
        self.resultLabel2.config(text=self.keys[1])
        self.resultLabel3.config(text=self.keys[2])
        self.resultLabel4.config(text=self.keys[3])
        self.resultLabel5.config(text=self.keys[4])
        self.resultLabel6.config(text=self.keys[5])
        
        self.resultValueLabel1.config(text=self.res[0])
        self.resultValueLabel2.config(text=self.res[1])
        self.resultValueLabel3.config(text=self.res[2])
        self.resultValueLabel4.config(text=self.res[3])
        self.resultValueLabel5.config(text=self.res[4])
        self.resultValueLabel6.config(text=self.res[5])

    def create_graph(self):
        """this method creates graphs and output them"""
        self.convert_spinbox_to_float()
        self.calculate_elements()

        revenue = [0, self.revenue]
        variable = [self.fixed, self.fixed + self.variable]
        fixed = [self.fixed, self.fixed]

        #graphs
        plt.plot(revenue)
        plt.plot(variable)
        plt.plot(fixed)

        #delete axes
        plt.xticks([])
        plt.yticks([])

        #output graphs
        plt.show()


def main():

    root = tk.Tk()
    root.title('calcCVP')
    root.geometry('600x350')
    app = Application(root=root)
    app.mainloop()
    

if __name__ == '__main__': main()