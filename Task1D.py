from floodsystem import geo, stationdata


def run():
    """Requirements for Task 1D"""
    output= geo.rivers_with_stations(stationdata.build_station_list())
    print(sorted(output))
    print(len(output))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()