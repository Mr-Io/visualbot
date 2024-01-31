import math

from prod import Resource

class Defence():
    def __init__(self, name="", cname="", img=None, cost=None, speed=0, cargo=0, build_s=0):
        self.name = name
        self.cname = cname
        self.img = img
        self.speed = speed
        self.cargo = cargo
        self.build_s = build_s
        self.number = 0
        self.buildable = False
        self.maxlim = 0
        self.cost=cost
    
    def __str__(self):
        return self.cname
    
    __repr__ = __str__


ROCKET_LAUNCHER = Defence(name="",
                          cname="Rocket Launcher",
                          img="images/rocket_launcher.png",
                          cost=Resource(2000, 0, 0),
                          )
LIGHT_LASER = Defence(cname="Light Laser",
                      img="images/light_laser.png",
                          cost=Resource(1500, 500, 0),
                      )
HEAVY_LASER = Defence(cname="Heavy Laser",
                      img="images/heavy_laser.png",
                          cost=Resource(6000, 2000, 0),
                      )
GAUSS_CANNON = Defence(cname="Gauss Cannon",
                       img="images/gauss_cannon.png",
                       cost=Resource(20000, 15000, 2000),
                       )
PLASMA_TURRET = Defence(cname="Plasma Turret", 
                        img="images/plasma_turret.png",
                        cost=Resource(50000, 50000, 30000),
                        )
SMALL_SHIELD = Defence(cname="Small Shield Dome", 
                       img="images/small_shield.png",
                       cost=Resource(10000, 10000, 0),
                       ) 
LARGE_SHIELD = Defence(cname="Large Shield Dome", 
                       img="images/small_shield.png", # change
                       cost=Resource(50000, 50000, 0),
                       )
ANTIBALLISTIC_MISSILE = Defence(cname="Anti-Ballistic Missiles", 
                                img= "images/antiballistic_missile.png",
                                cost=Resource(8000, 0, 2000),
                                )

iterdefences = [ANTIBALLISTIC_MISSILE, LARGE_SHIELD, SMALL_SHIELD,  PLASMA_TURRET, GAUSS_CANNON, HEAVY_LASER, LIGHT_LASER, ROCKET_LAUNCHER]

# defense build for 1 RIP
ROCKET_LAUNCHER.maxlim = 50000
LIGHT_LASER.maxlim = 0
HEAVY_LASER.maxlim = 2000
GAUSS_CANNON.maxlim = 500
PLASMA_TURRET.maxlim = 500
LARGE_SHIELD.maxlim = 1
SMALL_SHIELD.maxlim = 1
ANTIBALLISTIC_MISSILE.maxlim = math.inf