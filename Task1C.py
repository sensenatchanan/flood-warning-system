from floodsystem import geo, stationdata


def run():
    """Requirements for Task 1C"""
    stations = geo.stations_within_radius(stationdata.build_station_list(), (52.2053, 0.1218), 10)
    output = [(s.name) for (s) in stations]
    print(sorted(output))


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()