import numpy as np

def calculate_y(formula, x, a=0, b=0, c=0):
    if formula == 'linear':
        return a * x + b
    elif formula == 'quadratic':
        return a * x**2 + b * x + c
    else:
        return np.zeros_like(x)
