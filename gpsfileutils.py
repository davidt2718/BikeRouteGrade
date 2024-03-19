'''Module to extract data from GPX files'''
# NOTE If there is time/velocity data with the GPX, can probably use that to clean the data a bit

import gpxpy  # GPX parser library  https://pypi.org/project/gpxpy/

def readGpx(filepath):
    """Just read GPX in to a data file"""
    # Lat, Long, Alt, Time, Speed?  should be enough for processing/filtering GPS data
    pass


def getPositionFromGpx():
    """Get Lat, Long, Altitude data from GPX file and put in to a convenient format"""
    pass

