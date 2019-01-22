from floodsystem import geo, stationdata


def run():
    """Requirements for Task 1D"""
    output= geo.rivers_with_stations(stationdata.build_station_list())
    sorted_output = sorted(output)
    print(sorted_output[:10])
    print('\n number of rivers with at least one station is',  len(output))
    rivers = geo.stations_by_river(stationdata.build_station_list())
    
    print('River Aire:', sorted(rivers["River Aire"]))
    print('\n River Cam:', sorted(rivers["River Cam"]))
    print('\n Thames:', sorted(rivers["River Thames"]))



if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()