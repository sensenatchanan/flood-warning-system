from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_highest_rel_level

s_id = "test-s-id"
m_id = "test-m-id"
label = "some station"
coord = (1, 5)
trange = (-2.3, 3.4445)
river = "River X"
town = "My Town"
s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
s1.latest_level = 20.0
    
s_id = "test-s-id"
m_id = "test-m-id"
label = "some station"
coord = (52.2053, 0.1218)
trange = (-2.3, 3.4445)
river = "River X"
town = "My Town"
s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
s2.latest_level = 2.0

s_id = "test-s-id"
m_id = "test-m-id"
label = "some station"
coord = (52.2053, 0.1218)
trange = (-2.3, 3.4445)
river = "River X"
town = "My Town"
s3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
s3.latest_level = 50.0
s_id = "test-s-id"
m_id = "test-m-id"
label = "some station"
coord = (52.2053, 0.1218)
trange = (-2.3, 3.4445)
river = "River X"
town = "My Town"
s4 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
s4.latest_level = 1.0

l = (s1,s2,s3,s4)

def test_hishest():
    a = stations_highest_rel_level(l,3)
    m1 = a[0]
    r1 = m1[1]
    m2 = a[1]
    r2 = m2[1]
    m3 = a[2]
    r3 = m3[1]

    assert len(a)==3
    assert r1 > r2
    assert r2 > r3
