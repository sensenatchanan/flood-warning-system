from .utils import sorted_by_key
from floodsystem.analysis import slope_finder
#from .station import typical_range_consistent, relative_water_level

def stations_level_over_threshold(stations, tol):
        output_list = []
        for station in stations:
            if station.typical_range_consistent() == True:
                relative_level = station.relative_water_level()
                if relative_level is not None and relative_level > tol:
                    output_tuple = (station.name , relative_level)
                    output_list.append(output_tuple)
            else:
                pass
        return sorted_by_key(output_list, 1, reverse= True)

def stations_highest_rel_level(stations, N):
    output_list = []
    for station in stations:
        if station.typical_range_consistent() == True:
            relative_level = station.relative_water_level()
            if relative_level is not None: 
                output_tuple = (station.name , relative_level)
                output_list.append(output_tuple)
        else:
            pass
    result = sorted_by_key(output_list, 1, reverse= True)
    return result[:N]

def flood_risk(station):
    """This fuction calculates the risk index for a particular station"""
    
    level = station.relative_water_level()
    risk = 0
    rise = slope_finder(station)
    if level != None:
        if level > 10.0:
            risk = 4
        
        if level <= 10.0 and level >1.0:
            if rise == True:
                risk = 4
            else:
                risk = 3 
        
        if level <= 1.0 and level >0.5:
            if rise == True:
                risk = 3
            else:
                risk = 2
        
        if level<= 0.5:
            if rise == True:
                risk = 2
            else:
                risk = 1
    return risk

def risk_town_average(town_list):
    """This fuction takes the list of stations in the same town to calculate
    an averaged risk value"""
    town_risk = 0 
    N = 0
    for s in town_list:
        level = s.relative_water_level
        if level != None:
            town_risk += flood_risk(s)
            N += 1
    if N > 0:
        average_town_risk = town_risk/N
    else:
        average_town_risk = 0
    return average_town_risk

def town_by_risk(dictionary):
    """This function extracts the list of stations of the town from a
    dictionary and calculate the town's average risks value. Finally, return
    as a list of tuples consists of (town,risk value)"""
    towns_risk =[]
    for town in dictionary:
        town_risk = risk_town_average(dictionary[town])
        towns_risk.append((town, town_risk))
    return towns_risk
        