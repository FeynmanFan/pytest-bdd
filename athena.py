from robot import robot
from velocity import velocity

class athena(robot):
    def __init__(self, velocity = velocity(0,0)):
        robot.__init__(self, velocity)
        self.loadLimit = 480
        self.model = "athena"
        self.id = 1
        self.amperageLimit = 2
