class velocity:
    # heading is in degrees from magnetic north (determined from mGPS)
    def __init__(self, heading, speed):
        self.heading = heading % 360; # you can get more than 360 degrees sometimes with vector math, so this fixes that

        if speed < 0:
            raise Exception("Speed cannot be negative")

        self.speed = speed; # no negative speeds allowed

        pass