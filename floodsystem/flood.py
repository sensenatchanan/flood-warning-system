from .utils import sorted_by_key
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

