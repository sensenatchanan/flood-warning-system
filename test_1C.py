from floodsystem import geo, stationdata

def test_within_radius_true():
    """test the function to see if a station that is known to be within a certain radius is in the output"""
    stations = geo.stations_within_radius(stationdata.build_station_list(), (52.2053, 0.1218), 10)
    assert 'Girton' in [s.name for s in stations]

def test_within_radius_false():
    """test the function to see if a station that is known to be outside a certain radius is not in the output"""
    stations = geo.stations_within_radius(stationdata.build_station_list(), (52.2053, 0.1218), 10)
    assert 'Penzance Tesco' not in [s.name for s in stations]