# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine

def stations_by_distance(stations, p):
    """ Function that calculates the distance from the stations to a point and sorts them """
    result = []
    for station in stations:
        distance = haversine(p, station.coord)
        result.append((station, distance))
    #sort by distance
    return sorted_by_key(result, 1)

def stations_within_radius(stations, centre, r):
    """ function that returns a list of all stations within a certain radius of a point """
    output = []
    for station in stations:
        distance = haversine(centre, station.coord)
        if distance <= r:
            output.append(station)
    return output

def rivers_with_stations(stations):
    output = set((s.river) for (s) in stations)
    return output

def stations_by_river(stations):
   #rivers = set((s.river) for (s) in stations)
    #data = set(((s.river),(s.name)) for (s) in stations)
    results = [[s.name, s.town] for (s) in stations]


    #d = {(s.river):(s.name) for (s) in stations}
    return results