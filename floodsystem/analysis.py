import matplotlib as plt
import numpy as np 

def polyfit(dates, levels, p):

    #Converts data to floats
    x = plt.dates.date2num(dates)

    #Using shifted values, consider the coefficient
    p_coeff = np.polyfit(x-x[0],levels,p)
    
    poly = np.poly1d(p_coeff)
    d0 = x[0]

    return poly, d0

def slope_finder(station):
    """ This function computes the slope of a least-squares fit of polynomial
    of degree p to water level data and return that is it positive or negative"""
    try:
        dt = 2
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        slope = polyfit(dates,levels,1)
        if slope[1] >= 0:
            return True
        else:
            return False
    except:
        return None
    