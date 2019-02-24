import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import date2num

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

