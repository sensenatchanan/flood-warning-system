from floodsystem.geo import *
from floodsystem.stationdata import build_station_list

def test_stations_by_distance():
    """test if the stations are sorted correctly by distance"""
    station_list = build_station_list()
    #test for stations closest to cambridge city coordinates
    station_list_sort = stations_by_distance(station_list, (52.2053, 0.1218))
    output = [(station.name, distance) for (station, distance) in station_list_sort]
    for n in range(1, len(station_list)):
        #make sure that the distance of the previous station to the point is less than the next one in the list
        assert output[n-1][1] <= output[n][1]