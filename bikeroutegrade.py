import gpxpy  # GPX parser library  https://pypi.org/project/gpxpy/
import scipy.signal

# import rdp


def readGpx(filepath):
    """Just read GPX in to a data file"""
    pass


def getPositionFromGpx():
    """Get Lat, Long, Altitude data from GPX file and put in to a convenient format"""
    pass


def getDistances():
    """Point-to-point and cumulative distances"""
    #NOTE might have to import some sort of GPS data package
    pass


def smoothtrack():
    """Smooth out a length vs altitude track"""
    pass


def lineSegmentFit():
    """Returns a series of points that approximates the 2D path provided"""
    # https://en.wikipedia.org/wiki/Ramer–Douglas–Peucker_algorithm
    # https://github.com/fhirschmann/rdp
    # LATER come up with a scoring/minimization problem that balances no. of points vs. closeness to the path
    # for now, just use the traditional implementation of going until no points are outside a defined error gap


def findChangePoints():
    """Find peaks and places where slope changes significantly"""
    # Then, merge those lists of points.  Prioritize using peak points?
    # Note, peaks and valleys should show up as places of peak acceleration
