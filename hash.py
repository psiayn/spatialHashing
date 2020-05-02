"""
    Handles spatial hashing
"""

from collections import defaultdict

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


class SpatialHashTable():
    """
    Creates a spatial hash table
    """
    def __init__(self, cell_size):
        self.cell_size = cell_size
        self.spatialHash = defaultdict(list)

    def _hash(self, x, y):
        return int(x/self.cell_size), int(y/self.cell_size)

    def get_x(self, obj):
        return obj.x

    def get_y(self, obj):
        return obj.y

    def insertObject(self, obj):
        self.spatialHash[self._hash(self.get_x(obj), self.get_y(obj))].append(obj)

    def insertObject_pos(self, obj, x, y):
        self.spatialHash[self._hash(x, y)].append(obj)

    def removeObject(self, obj):
        self.spatialHash[self._hash(self.get_x(obj), self.get_y(obj))].remove(obj)

    def removeObject_pos(self, x, y, obj):
        self.spatialHash[self._hash(x, y)].remove(obj)

    def updateObject(self, obj, new_x, new_y):
        self.removeObject(obj)
        self.insertObject_pos(obj, new_x, new_y)

    def search_in_box(self, x_min, x_max, y_min, y_max):
        _min, _max = self._hash(x_min, y_min), self._hash(x_max, y_max)
        found_objects = []
        for i in range(_min[0], _max[0]+1):
            for j in range(_min[1], _max[1]+1):
                found_objects.extend(self.spatialHash[i, j])
        return found_objects

    def search_nearby(self, obj, half_range):
        x = self.get_x(obj)
        y = self.get_y(obj)
        return self.search_in_box(x - half_range, x + half_range,
                                  y - half_range, y + half_range)

