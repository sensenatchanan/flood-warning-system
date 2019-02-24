# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""

class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
    def typical_range_consistent(self):
        """method returns false if typical range data is inconsistent"""
        return not (self.typical_range is None or (self.typical_range[1] < self.typical_range[0]))

    def relative_water_level(self):
        """method that returns the latest water levels as a fraction of its typical range"""
        if self.typical_range is None or (self.typical_range[1] < self.typical_range[0]) or self.latest_level is None:
            return None
        else:
            height_range = self.typical_range[1] - self.typical_range[0]
            return (self.latest_level - self.typical_range[0])/height_range



def inconsistent_typical_range_stations(stations):
    """function which returns a list of all stations with inconsistent range data"""
    inconsistent_stations = []
    for station in stations:
        if station.typical_range_consistent() == False: 
            inconsistent_stations.append(station.name)
    return sorted(inconsistent_stations)