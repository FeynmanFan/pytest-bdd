class gripperArm:
    INCLINATION_ROTATION_ANGLE_LIMIT = 25

    def __init__(self, inclination = 0, errorState = "None", gripState = "open"):
        self._inclination = inclination
        self._errorState = errorState
        self._gripState = gripState

    def _get_inclination(self):
        return self._inclination
    
    def _set_inclination(self, value):
        self._autoOriented = False
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

    def _get_gripState(self):
        return self._gripState
    
    def _set_gripState(self, value):
        self._gripState = value

    gripState = property(
        fget = _get_gripState,
        fset = _set_gripState,
        doc="The state reflecting whether the gripper arm is closed or not."
    )

    def close(self):
        self.gripState = "closed"

    def open(self):
        self.gripState = "open"

    def rotate(self, degrees):
        if (self.inclination >= self.INCLINATION_ROTATION_ANGLE_LIMIT and self.gripState == "closed"):
            self.autoOrient()
            #self.errorState = "INCLINATION_ROTATION_ANGLE_LIMIT"
            #raise Exception("INCLINATION_ROTATION_ANGLE_LIMIT exceeded in rotation")
        # rotation logic

    def autoOrient(self):
        self.inclination = 0
        self._autoOriented = True