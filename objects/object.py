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
