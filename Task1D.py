from floodsystem import geo, stationdata


def run():
    """Requirements for Task 1D"""
    output= geo.rivers_with_stations(stationdata.build_station_list())
    print(sorted(output))
    print(len(output))
    rivers = geo.stations_by_river(stationdata.build_station_list())
    
    
    print(sorted(rivers["River Thames"]))



if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()