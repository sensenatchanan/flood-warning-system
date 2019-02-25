import datetime
import matplotlib.pyplot as plt
import numpy as np
from .analysis import polyfit
from matplotlib.dates import date2num
import matplotlib

def plot_water_levels(station, dates, levels):
    if levels != None:
        plt.plot(dates, levels, '-b')
        plt.hlines(levels[0], dates[0], dates[-1], 'g', label = 'typical low')
        plt.hlines(levels[1], dates[0], dates[-1], 'r', label = 'typical high')
    else:
        plt.plot(dates, levels, '-b')

    plt.xlabel('Date')
   
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.legend()
    plt.show()

"Task 2F"
def plot_water_level_with_fit(station, dates, levels, p):
    """ This function plots the water level data and the best-fit polynomial
        Given the water level time history (dates, level), this function allows
        the plot of the data's best-fit polynomial, with a desired power p."""
    x = matplotlib.dates.date2num(dates)
    #oly = polyfit.poly(dates, levels, p)
    #d0 = polyfit.d0(dates, levels, p)
    
    a,b = polyfit(dates, levels, p)
    
    #plot original data points
    plt.plot(x,levels,'.')
    
    #Plot polynomial fit
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, a(x1-b))
    
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.title(station.name)
    
    #Lower, Upper = station.typical_range
    #plt.plot(Lower,levels)
    #plt.plot(Upper,levels)
    
    plt.show()
