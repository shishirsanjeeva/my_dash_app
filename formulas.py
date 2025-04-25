import numpy as np


def calculate_y(formula, sigma_mean, sigma_alt, strength) -> float:
    if formula == 'GM':
        return sigma_alt / (1 - (sigma_mean/strength))
    elif formula == 'SB':
        return sigma_alt / (1 - (sigma_mean/strength))
    else:
        return Nones