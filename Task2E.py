import datetime
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels

def run():
    stations = build_station_list()
    station_dict = {s.name: s for s in stations}
    update_water_levels(stations)

    #select the 5 highest stations for relative water levels
    highest_stations = [station_dict[s[0]] for s in stations_highest_rel_level(stations, 5)]
    dt = 10

    for station in highest_stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(station, dates, levels)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()