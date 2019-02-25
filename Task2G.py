from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import town_by_risk
from floodsystem.geo import stations_by_town

""""
In this task, the towns with the greatest risk of flooding will be given
"""

def run():
    
    """First,based on the relative water level of each station, each station
    will be given a "risk assessment mark". The high the mark, the more likely
    flooding is going to occur. Then, all rivers in a given town will be
    gathered and give an averaged score
    
    Severe rating: x > 3 -- (for relative water level >10)
    High rating: 2 < x <= 3 -- (for relative water level <= 10 and >1)
    Mid rating: 1 < x <= 2 -- (for relative water level <= 1 and >0.5)
    Low rating: 0 < x <= 1 -- (for relative water level <0.5)
    
    """
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)
    
    town_dict = stations_by_town(stations)
    #print(town_dict)
    
    values = town_by_risk(town_dict)

    severe = []
    high = []
    mid = []
    low = []
    
    for figure in values: 
        
        if figure[1] > 3:
            severe.append(figure[0])
        if figure[1] > 2 and figure[1] <= 3:
            high.append(figure[0])
        if figure[1] > 1 and figure[1] <= 2:
            mid.append(figure[0])
        if figure[1] > 0 and figure[1] <= 1 :
            low.append(figure[0])
        
    print("The towns with warning 'severe': ", severe)
    print("The towns with warning 'high': ", high)
    print("The towns with warning 'mid': ", mid)
    print("The towns with warning 'low': ", low)
        
    
if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()