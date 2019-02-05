from floodsystem import station
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key

def test_consistent_typial_range_stations():
    stations = build_station_list()
    inconsistent_stations = station.inconsistent_typical_range_stations(stations)
    assert 'Apperly Bridge' not in inconsistent_stations

def test_inconsistent_typical_range_stations():
    stations = build_station_list()
    inconsistent_stations = station.inconsistent_typical_range_stations(stations)
    assert 'Addlestone' in inconsistent_stations