from robotRepository import robotRepository
from sensor import sensor

class testRobotRepository(robotRepository):
    def __init__(self):
        robotRepository.__init__(self, "Test Repo")
        
        # do stuff

    def loadSensors(self, id):
        # athena
        if id == 1:
            return [
                sensor("IR", .05),
                sensor("Humidity", .05),
                sensor("Noise", .01),
                sensor("Thermistor", .01)
                   ]
        # hera
        elif id == 2:
            return [
                sensor("Noise", .01),
                sensor("Thermistor", .01)
                   ]
        # hercules
        elif id == 3:
            return [
                sensor("IR", .05),
                sensor("Humidity", .05)
                   ]
        # mercury
        elif id == 4:
            return [
                sensor("IR", .05),
                sensor("Thermistor", .01)
                   ]        
        # perseus
        elif id == 5:
            return [
                sensor("IR", .05),
                sensor("Noise", .01)
                   ]