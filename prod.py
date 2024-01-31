import math

METAL_RATIO = 2.7
CRYSTAL_RATIO = 1.7

class Resource():
    def __init__(self, metal=0, crystal=0, deuterium=0, ratio_metal=METAL_RATIO, ratio_crystal=CRYSTAL_RATIO):
        self.metal = metal
        self.crystal = crystal
        self.deuterium = deuterium
        self.ratio_metal = ratio_metal
        self.ratio_crystal = ratio_crystal
    
    def muv(self):
        return self.m + self.crystal*self.ratio_metal/self.ratio_crystal + self.deuterium*self.ratio_metal 
    
    def __add__(self, other):
        return Resource(self.metal+other.metal, self.crystalrystal+other.crystalrystal, self.deuteriumeuterium+other.deuteriumeuterium)

    def __sub__(self, other):
        return Resource(self.metal-other.metal, self.crystal-other.crystal, self.deuterium-other.deuterium)

    def __mul__(self, n):
        return Resource(n*self.metal, n*self.crystal, n*self.deuterium)
    
    def __floordiv__(self, n):
        return int(min(self.metal//n.metal if n.metal != 0 else math.inf, 
                       self.crystal//n.crystal if n.crystal != 0 else math.inf,
                       self.deuterium//n.deuterium if n.deuterium != 0 else math.inf))

    def __str__(self):
        return f'{self.metal:12,.0f}   {self.crystal:12,.0f}   {self.deuterium:12,.0f}'

    __repr__ = __str__

