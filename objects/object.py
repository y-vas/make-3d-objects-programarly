import random ,math, os
from random import randint

class Object():
    def __init__(self, size = 5, name = "build"):
        self.NAME = name;
        self.START_POINTS = 20;
        self.VERTICES = [];      # [Vector(x,y,z), id ]
        self.FACES = [];         # [[id1, id2..] , id ]
        self.MATERIALS = [];     # [mat.., [fid, fid2]]
        self.DELIMITERS = []
        self.NORMALIZED_ANGLES = 60
        self.SIZE = size
        self.STRUC_HEIGHT = 2
        self.IDS = 0;

    def example_cube(self):

        CUBE_POINTS = (
            (0.5, -0.5, -0.5 ),
            (0.5, 0.5, -0.5 ),
            (-0.5, 0.5, -1 ),
            (-0.5, -0.5, -0.5 ),
            (0.5, -0.5, 0.5 ),
            (0.5, 0.5, 0.5 ),
            (-0.5, -0.5, 0.5 ),
            (-0.5, 0.5, 0.5 ),
        )

        # colors are 0-1 floating values
        CUBE_COLORS = (
            (1, 0, 0),
            (1, 1, 0),
            (0, 1, 0),
            (0, 0, 0),
            (1, 0, 1),
            (1, 1, 1),
            (0, 0, 1),
            (0, 1, 1),
        )

        CUBE_QUAD_VERTS = (
            (0, 1, 2, 3),
            (3, 2, 7, 6),
            (6, 7, 5, 4),
            (4, 5, 1, 0),
            (1, 5, 7, 2),
            (4, 0, 3, 6),
        )

        CUBE_EDGES = (
            (0, 1), (0, 3), (0, 4),
            (2, 1), (2, 3),
            (2, 7), (6, 3),
            (6, 4), (6, 7), (5, 1),
            (5, 4), (5, 7),
        )

        return CUBE_EDGES,CUBE_POINTS,CUBE_QUAD_VERTS,CUBE_COLORS
