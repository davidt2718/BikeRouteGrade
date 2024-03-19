"""Module to extract data from GPX files"""

# NOTE If there is time/velocity data with the GPX, can probably use that to clean the data a bit

import gpxpy as gp  # GPX parser library  https://pypi.org/project/gpxpy/
from geopy import distance
import pandas as pd
import numpy as np
from routecolumns import rcol


def readGpx(filepath):
    """Just read GPX in to a data file"""
    # Lat, Long, Alt, Time, Speed?  should be enough for processing/filtering GPS data
    with open(filepath) as file:
        gpxfile = gp.parse(file)

    # Determine if this is a track or route GPX

    data = None

    #TODO Deal with more than one track, segment, or route
    for p in gpxfile.tracks[0].segments[0].points:
        input = [
            [p.latitude, p.longitude, p.elevation, p.time, (p.latitude, p.longitude)]
        ]
        if data is None:
            data = np.array(input)
        else:
            data = np.append(data, input, axis=0)

    data = pd.DataFrame(
        data,
        columns=[
            rcol.latitude,
            rcol.longitude,
            rcol.elevation,
            rcol.time,
            rcol.latlong,
        ],
    )
    data[rcol.dist] = getpointdist(df=data)
    data[rcol.cumdist] = data[rcol.dist].cumsum()
    data[rcol.cumtime] = data[rcol.time] - min(data[rcol.time])

    # buildprofile(df=data)

    return data


def getpointdist(df: pd.DataFrame) -> pd.Series:
    dist = np.vectorize(distance.distance)

    distdata = dist(df[rcol.latlong], df.shift(1)[rcol.latlong])
    distdata = [p.m for p in distdata]
    distdata[0] = 0
    return distdata