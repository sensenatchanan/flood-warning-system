from floodsystem import geo, stationdata


def run():
    """Requirements for Task 1D"""
    output= geo.rivers_with_stations(stationdata.build_station_list())
    sorted_output = sorted(output)

    #Print no. of rivers with stations
    print('\nNumber of rivers with at least one station is',  len(output), ". \n")
    #Print first 10 stations
    print("First 10 rivers with stations: \n", sorted_output[:10])
    rivers = geo.stations_by_river(stationdata.build_station_list())
    
    #Print stations on the following rivers
    print('\nRiver Aire: \n', sorted(rivers["River Aire"]))
    print('\nRiver Cam: \n', sorted(rivers["River Cam"]))
    print('\nThames: \n', sorted(rivers["River Thames"]))



if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()