from floodsystem.analysis import polyfit
import numpy as np
import matplotlib
from datetime import datetime, timedelta
import matplotlib.dates


def test_polyfit():
    y = [0.1, 0.09, 0.23, 0.34, 0.78, 0.74, 0.43]
    p=4
    x = [datetime(2016, 12, 30), datetime(2016, 12, 31), datetime(2017, 1, 1),
        datetime(2017, 1, 2), datetime(2017, 1, 3), datetime(2017, 1, 4),
        datetime(2017, 1, 5)]
    c = polyfit(x,y,p)
    z = matplotlib.dates.date2num(x)
    p_coeff = np.polyfit(z-z[0], y, p)
    a = np.poly1d(p_coeff)
    b = z[0]
    c = polyfit(x,y,p)
    d = a,b
    assert c == d
