from robot import robot
from velocity import velocity

class mercury(robot):
    def __init__(self, velocity = velocity(0,0)):
        robot.__init__(self, velocity)
        self.loadLimit = 100
        self.model = "mercury"
        self.id = 4
        self.amperageLimit = .075