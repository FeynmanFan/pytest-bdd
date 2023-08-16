from velocity import velocity
from gripperArm import gripperArm
from robotRepository import robotRepository

class robot:
    def __init__(self, velocity = velocity(0,0)):
        self.velocity = velocity;
        self.gripperArm = gripperArm();
        self.loadState = "NORMAL"
        self.loadLimit = 0
        self.model = "BASE"
        self.amperageLimit = 0
        self.powerState = "UNKNOWN"
        #self.repo = robotRepository()

    @staticmethod
    def _set_repo(self, value):
        self._repo = value
        
    @staticmethod
    def _get_repo(self):
        return self._repo
    
    repo = property(
        fget = _get_repo,
        fset = _set_repo
    )

    def checkAmperage(self):
        sensors = self.repo.loadSensors(self.id)

        totalSensorAmperage = sum(s.amperage for s in sensors)
        if (totalSensorAmperage > self.amperageLimit):
            self.powerState = "OVERLOAD"
        else:
            self.powerState = "ALL"

    def motionEvaluation(self, nearfieldDetected = False):
        # do a bunch of stuff that is unrelated to the current issue
        if nearfieldDetected:
            if (self.velocity.speed  > 0):
                self.velocity.speed -= 1
            pass            

    def _get_powerState(self):
        return self._powerState

    def _set_powerState(self, value):
        self._powerState = value

    powerState = property(
        fget = _get_powerState,
        fset = _set_powerState
    )

    def _get_loadState(self):
        return self._loadState

    def _set_loadState(self, value):
        self._loadState = value

    loadState = property(
        fget = _get_loadState,
        fset = _set_loadState
    )
    
    def _get_amperageLimit(self):
        return self._amperageLimit

    def _set_amperageLimit(self, value):
        self._amperageLimit = value

    amperageLimit = property(
        fget = _get_amperageLimit,
        fset = _set_amperageLimit
    )

    def _get_loadLimit(self):
        return self._loadLimit
    
    def _set_loadLimit(self, value):
        self._loadLimit = value

    loadLimit = property(
        fget = _get_loadLimit,
        fset = _set_loadLimit
    )

    def _get_model(self):
        return self._model
    
    def _set_model(self, value):
        self._model = value

    model = property(
        fget = _get_model,
        fset = _set_model
    )

    def load(self, loadWeight):
        if (loadWeight > self.loadLimit):
            self.loadState = "OVERLOAD"
    
    def _get_gripperArm(self):
        return self._gripperArm
    
    def _set_gripperArm(self, value):
        self._gripperArm = value

    gripperArm = property(
            fget = _get_gripperArm,
            fset = _set_gripperArm,
            doc="The object property for the gripper arm."
    )