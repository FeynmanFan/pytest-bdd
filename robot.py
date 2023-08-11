import velocity
from gripperArm import gripperArm

class robot:
    def __init__(self, velocity):
        self.velocity = velocity;
        self.gripperArm = gripperArm();

    def motionEvaluation(self, nearfieldDetected = False):
        # do a bunch of stuff that is unrelated to the current issue
        if nearfieldDetected:
            if (self.velocity.speed  > 0):
                self.velocity.speed -= 1
            pass            
    
    def _get_gripperArm(self):
        return self._gripperArm
    
    def _set_gripperArm(self, value):
        self._gripperArm = value

    gripperArm = property(
            fget = _get_gripperArm,
            fset = _set_gripperArm,
            doc="The object property for the gripper arm."
    )