
from floodsystem import flood, stationdata

def run():
    # Build list of stations
    stations = stationdata.build_station_list()
    # Update latest level data for all stations
    stationdata.update_water_levels(stations)
    print (flood.stations_level_over_threshold(stations, 0.8))


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()

