from robot import robot
from velocity import velocity

class hera(robot):
    def __init__(self, velocity = velocity(0,0)):
        robot.__init__(self, velocity)
        self.loadLimit = 300
        self.model = "hera"
        self.id = 2
        self.amperageLimit = .04

