from floodsystem import geo, stationdata


def run():
    output = geo.rivers_by_station_number(stationdata.build_station_list(), N=9)
    print(output)

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()