import velocity

class robot:
    def __init__(self, velocity):
        self.velocity = velocity;
        print("init")

    def motionEvaluation(self, nearfieldDetected = False):
        # do a bunch of stuff that is unrelated to the current issue
        if nearfieldDetected:
            self.velocity.speed -= 1
        else:
            pass            
    