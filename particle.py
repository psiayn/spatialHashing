"""
Handles particle behaviour
"""


from random import randint

class Particle:
    """
    Initializes a 2D particle with it's center co-ordinates

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

    def move(self):
        self.x += randint(-2, 2)
        self.y += randint(-2, 2)
