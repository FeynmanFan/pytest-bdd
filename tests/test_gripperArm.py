import pytest
from robot import robot
from velocity import velocity

@pytest.fixture
def the_robot():
    return robot(velocity(0,0))


def test_rotateArmAtZeroInclination(the_robot):
    the_robot.gripperArm.inclination = 0
    the_robot.gripperArm.rotate(10)

    # no error raised
    assert True == True

def test_rotateArmAtFortyDegreeInclination(the_robot):
    the_robot.gripperArm.inclination = 40
    with pytest.raises(Exception) as e:
        the_robot.gripperArm.rotate(10)

    print(str(e.value))
    assert str(e.value) == "INCLINATION_ROTATION_ANGLE_LIMIT exceeded in rotation"
    assert the_robot.gripperArm.errorState == "INCLINATION_ROTATION_ANGLE_LIMIT"

def test_autoOrient(the_robot):
    the_robot.gripperArm.autoOrient()

    assert the_robot.gripperArm._autoOriented == True

