import matplotlib as plt
import numpy as np 

def polyfit(dates, levels, p):
    dates = plt.dates.date2num(dates)
    x = np.linspace(max(dates, min(dates), len(dates))
    d0 = x[0]
    p_coeff = np.polyfit(x-d0, levels, p)
    poly = np.poly1d(p_coeff)
    return poly, x 