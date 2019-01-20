# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

def stations_by_distance(stations, p):
    result = []
    (x0, y0) = p
    for station in stations:
        (x1, y1) = station.coord
        distance = ((x0 - x1)**2 + (y0 - y1)**2)**(1/2)
        result.append((station, distance))
    return sorted_by_key(result, 1)