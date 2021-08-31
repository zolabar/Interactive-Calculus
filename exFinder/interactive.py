# -*- coding: utf-8 -*-
from ipywidgets import interactive, interact
import matplotlib.pyplot as plt
import numpy as np
import ipywidgets as widgets
import sympy as sym
import seaborn as sns
import plotly.graph_objects as go
from plotly.offline import init_notebook_mode, iplot
from numba import jit

jit(nopython=True, parallel=True)


class plot_sine():
    
    def __init__(self, preWidgetN):
        
        self.N = preWidgetN
        
        x,y,n ,k = sym.symbols('x, y,n,k', real=True)
        X=np.linspace(0, 10, 100)
        
        f = sym.Sum((-1)**k*(x**(2*k+1))/(sym.factorial(2*k+1)),(k,0, n))
        f = f.subs(n, self.N.value)
        f = sym.lambdify(x, f)
        self.trace1 = go.Scatter(x=X, y=np.sin(X),
                            mode='lines+markers',
                            name='sin'
                               )
        self.trace2 = go.Scatter(x=X, y=f(X),
                            mode='lines',
                            name='sin-series till {0}'.format(self.N.value)
                               )

        self.fig = go.FigureWidget(data=[self.trace1, self.trace2], layout = go.Layout(template='plotly_dark'))
        
        #print(self.N)
        #print(self.N.value)

    def sineSeries(self, change):

        x,y,n ,k = sym.symbols('x, y,n,k', real=True)
        X=np.linspace(0, 10, 100)
        f = sym.Sum((-1)**k*(x**(2*k+1))/(sym.factorial(2*k+1)),(k,0, n))
        f = f.subs(n, self.N.value)
        f = sym.lambdify(x, f)

        trace1 = go.Scatter(x=X, y=np.sin(X),
                        mode='lines+markers',
                        name='sin')
        trace2 = go.Scatter(x=X, y=f(X),
                        mode='lines',
                        name='sin-series till {0}'.format(self.N.value))


        with self.fig.batch_update():
            self.fig.data[0].x = X
            self.fig.data[0].y = np.sin(X)
            self.fig.data[0].mode = 'lines+markers'
            self.fig.data[0].name = 'sin'
            self.fig.data[1].x = X
            self.fig.data[1].y = f(X)
            self.fig.data[1].mode = 'lines'
            self.fig.data[1].name = 'sin-series till {0}'.format(self.N.value)

        return 
    
    def show(self):
        self.N.observe(self.sineSeries, names='value')
        display(self.N, self.fig)
        return

