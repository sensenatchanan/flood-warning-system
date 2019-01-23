# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem import geo, stationdata


def run():
    """Requirements for Task 1B"""
    stations = geo.stations_by_distance(stationdata.build_station_list(), (52.2053, 0.1218))
    results = [(s.name, s.town, distance) for (s, distance) in stations]
    print("10 closest stations from Cambridge: \n", results[:10])
    print("\n10 furthest stations from Cambridge: \n", results[-10:])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()