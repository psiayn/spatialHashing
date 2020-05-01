"""
    Handles spatial hashing
"""

class Point:
    """
    Initializes a 2D object with it's center co-ordinates

    Parameters
    -----------
    x : int
        X co-ordinate of the center of the point
    y : int
        Y co-ordinate of the center of the point
    radius(optional) : float
        Collision detector radius, set to 0 by default

    """
    def __init__(self, x, y, radius=0):
        self.x = x
        self.y = y
        self.radius = radius


class HashTable:
    """
    Creates a spatial hash table

    Functions
    ------------

    insertObject(point)
        inserting a point into the hash table


    """
    def __init__(self, cell_size, width, height):
        self.cell = cell_size
        self.w = width
        self.h = height
        self.spatialHash = dict()

    def _hash(self, point):
        return int(point.x/self.cell), int(point.y/self.cell)

    def insertObject(self, point):
        self.spatialHash.setdefault(self._hash(point), []).append(point)
