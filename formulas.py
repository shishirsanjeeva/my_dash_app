import numpy as np


def calculate_y(formula, sigma_mean, sigma_alt, strength):
    if formula == 'GM':
        return fatigue_limit = simgma_alt / (1 - (sigma_mean/ultimate_strength))
    elif formula == 'SB':
        return fatigue_limit = simgma_alt / (1 - (sigma_mean/ultimate_strength))
    else:
        return np.zeros_like(x)