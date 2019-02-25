from floodsystem.station import MonitoringStation

s_id = "test-s-id"
m_id = "test-m-id"
label = "some station"
coord = (-3.0, 70)
trange = (2, 4)
river = "River B"
town = "My Town"
s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
s.latest_level = float(5)

def test_relative():
    r = s.relative_water_level()
    assert r == 1.5