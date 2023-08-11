class gripperArm:
    INCLINATION_ROTATION_ANGLE_LIMIT = 25

    def __init__(self, inclination = 0, errorState = ""):
        self._inclination = inclination
        self._errorState = errorState

    def _get_inclination(self):
        return self._inclination
    
    def _set_inclination(self, value):
        self._inclination = value

    inclination = property(
        fget = _get_inclination,
        fset = _set_inclination,
        doc="The inclination value for the gripper arm."
    )

    def _get_errorState(self):
        return self._errorState
    
    def _set_errorState(self, value):
        self._errorState = value

    errorState = property(
        fget = _get_errorState,
        fset = _set_errorState,
        doc="The errorstate for the gripper arm."
    )

    def rotate(self, degrees):
        if (self.inclination > self.INCLINATION_ROTATION_ANGLE_LIMIT):
            self.errorState = "INCLINATION_ROTATION_ANGLE_LIMIT"
            raise Exception("INCLINATION_ROTATION_ANGLE_LIMIT exceeded in rotation")
        # rotation logic

    def autoOrient(self):
        self._autoOriented = True
        self.inclination = 0