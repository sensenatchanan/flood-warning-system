from floodsystem import geo
from floodsystem.stationdata import build_station_list

def test_river_by_station_number():
    """ Checks that a list of tuples is returned.
    Checks the length of output (output can be greater of equal to N if there
    are more rivers with the same number of stations as the Nth entry) """

    stations = build_station_list()
    assert type (geo.rivers_by_station_number(stations,10)[0]) == tuple
    assert len(geo.rivers_by_station_number(stations,10)) >= 10