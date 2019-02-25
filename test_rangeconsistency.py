from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.station import MonitoringStation

def test_range():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (52.2053, 0.1218)
    river = "River X"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, None, river, town)
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-3.0, 70)
    trange = (5, 3.4445)
    river = "River X"
    town = "My Town"
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (52.2053, 0.1218)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (52.2053, 0.1218)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s4 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (52.2053, 0.1218)
    trange = (8, 3.4445)
    river = "River X"
    town = "My Town"
    s5 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (52.2053, 0.1218)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s6 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    d=[s1,s2,s3,s4,s5,s6]
    l=inconsistent_typical_range_stations(d)
    n=len(l)
    
    assert n == 3
    
