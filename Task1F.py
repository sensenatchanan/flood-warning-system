from floodsystem import station, stationdata, geo

def run():
    """Requirements for Task 1F"""
    test = station.inconsistent_typical_range_stations(stationdata.build_station_list())
    print("Stations with inconsistent typical range data: \n", sorted(test))

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()