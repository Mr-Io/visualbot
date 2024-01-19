class Ship():
    def __init__(self, name, cname, img, speed=0, cargo=0, build_s=0):
        self.name = name
        self.cname = cname
        self.img = img
        self.speed = speed
        self.cargo = cargo
        self.build_s = build_s
        self.number = 0

BATTLECRUISER = Ship("battlecruiser",
                     "Battlecruiser",
                     "images/battlecruiser.png")
BATTLESHIP = Ship("",
                  "Battleship",
                  "images/battleship.png")
BOMBER = Ship("",
              "Bomber",
              "images/bomber.png")
COLONYSER = Ship("",
                 "Colony Ship",
                 "images/colonyser.png")
CRUISER = Ship("cruiser",
               "Cruiser",
               "images/cruiser.png")
DESTROYER = Ship("",
                 "Destroyer",
                 "images/destroyer.png")
ESP_PROBE = Ship("",
                 "Espionage Probe",
                 "images/esp_probe.png") # problem with fleets...
HEAVY_FIGHTER = Ship("",
                     "Heavy Fighter",
                     "images/heavy_fighter.png")
LIGHT_FIGHTER = Ship("",
                     "Light Fighter",
                     "images/light_fighter.png")
RECYCLER = Ship("",
                "Recycler",
                "images/recycler.png")
RIP = Ship("",
           "Deathstar",
           "images/rip.png")
SMALL_CARGO = Ship("",
                   "Small Cargo",
                   "images/small_cargo.png")
LARGE_CARGO = Ship("",
                   "Large Cargo",
                   "images/large_cargo.png", 
                   speed=27750, 
                   cargo=52623, 
                   build_s=4)
ALL_SHIPS = Ship("",
                 "",
                 "images/fleet_selectall.png")

iterships = (BATTLECRUISER, BATTLESHIP, BOMBER, COLONYSER, CRUISER, DESTROYER, ESP_PROBE, HEAVY_FIGHTER, LIGHT_FIGHTER, RECYCLER, RIP, SMALL_CARGO, LARGE_CARGO)