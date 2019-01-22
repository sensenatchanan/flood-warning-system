from floodsystem import geo, stationdata


def run():
    """Requirements for Task 1D"""
    output= geo.rivers_with_stations(stationdata.build_station_list())
    print(sorted(output))
    print(len(output))
    stations = geo.stations_by_river(stationdata.build_station_list())
    #print("\n", stations)
    print (stations)
    #rivercam = stations ["River Cam"]
    #print (rivercam)
    print ("\n", stations[0][1])
    
  

    #for n in range(len(stations)):
        
    n = 0
    station_list = []
    riverdict = [stations[n][0], station_list]
    station_list += stations[n][1]
    n += 1
    for n in range(len (stations)):
        if stations[n-1][0] == stations[n][0]:
            station_list += stations [n][0]
        n+= 1
    else: n+= 1
    print (riverdict)
        



if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()