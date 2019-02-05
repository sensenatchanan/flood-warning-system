from floodsystem import geo, stationdata

def test_1Di(): 
    assert geo.rivers_with_stations([stationdata.build_station_list()[0]]) == {'River Dikler'}

def test_1Dii():
    stations = stationdata.build_station_list()
    loc = 0
    for x in range(0, len(stations)):
        if (stations[x].name == 'River Dickler'):
            loc = x

    toTest = geo.stations_by_river([stations[loc]])
    stat = toTest.get('River Dikler')
    assert len(stat) == 1
    assert stat[0] == 'Bourton Dickler'