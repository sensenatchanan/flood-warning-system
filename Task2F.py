import datetime
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import update_water_levels
from floodsystem.utils import sorted_by_key
from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

def run():
    # Build list of stations
    stations = build_station_list()
    
      # Update latest level data for all stations
    update_water_levels(stations)
    
       # Find station 'Cam'
       
    results2 =[]
    fail2 = []
    for s in stations:
        r = MonitoringStation.relative_water_level(s)
        if r == None:
            fail2.append(s)
        else:
            results2.append((s.name,r))
    results2=sorted_by_key(results2,1,reverse=True)
    l = results2  
    print(l[0][0])
            
    for i in range (5):
        name = l[i][0]
        for s in stations:
            if s.name == name:
                station = s
        dt = 10
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))    
        Lower, Upper = station.typical_range
        print(Lower, Upper)
        
        x = matplotlib.dates.date2num(dates)
       
        plt.plot(dates,np.full(len(x),Lower))
        plt.plot(dates,np.full(len(x),Upper))
        plot_water_level_with_fit(station, dates, levels, 4)                                                                    
       
plt.show()

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    
    run()               