from robot import robot
from velocity import velocity

class hercules(robot):
    def __init__(self, velocity = velocity(0,0)):
        robot.__init__(self, velocity)
        self.loadLimit = 1000
        self.model = "hercules"
        self.id = 3
        self.amperageLimit = 2