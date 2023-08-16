from robot import robot
from velocity import velocity

class perseus(robot):
    def __init__(self, velocity = velocity(0,0)):
        robot.__init__(self, velocity)
        self.loadLimit = 400
        self.model = "perseus"
        self.id = 5
        self.amperageLimit = .07