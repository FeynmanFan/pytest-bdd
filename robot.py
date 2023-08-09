import velocity

class robot:
    def __init__(self, velocity):
        self.velocity = velocity;

    def motionEvaluation(self, nearfieldDetected = False):
        # do a bunch of stuff that is unrelated to the current issue
        if nearfieldDetected:
            if (self.velocity.speed  > 0):
                self.velocity.speed -= 1
            pass            
    