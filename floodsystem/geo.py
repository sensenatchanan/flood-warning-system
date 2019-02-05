# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine

def stations_by_distance(stations, p):
    """ Function that calculates the distance from the stations to a point and sorts them
    Inputs:
        stations : list of MonitoringStation objects
        p : coordinate centre
    Outputs:
        list of MonitoringStation objects sorted by distance"""
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
    """function that outputs all rivers with a monitoring station as a set """
    output = set([s.river for s in stations])
    return output

def stations_by_river(stations):
    """function that creates a dictionary for each river and its corresponding stations"""
    results = [[s.river, s.name] for s in stations]
    rivers = {}
    for river, station in results:
        if river in rivers:
            rivers[river].append(station)
        else:
            rivers[river] = [station]
    return rivers

def rivers_by_station_number(stations, N):
    """function that returns the N rivers with the greatest number of monitoring stations"""
    river_station_numbers = []
    rivers = stations_by_river(stations)
    for river in rivers:
        river_station_numbers.append((river, len(rivers[river])))
    station_sort = sorted_by_key(river_station_numbers, 1, reverse = True)
    
    while station_sort[N-1][1] == station_sort[N][1] and N <= len(station_sort):
        N += 1
    return station_sort[:N]

