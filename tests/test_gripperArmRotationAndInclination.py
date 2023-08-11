import pytest
from pytest_bdd import scenario, given, when, then, parsers
from robot import robot
from velocity import velocity
from gripperArm import gripperArm


@pytest.fixture
def the_robot():
	return robot(velocity(0,0))

@scenario("../features/gripperArmRotationAndInclination.feature", "The rotate feature is called when the arm is closed and with different inclination values")
def test_inclination():
	return

@given(parsers.parse("the gripper arm inclination is {inclination: d}"))
def setInclination(the_robot, inclination):
	the_robot.gripperArm.inclination = inclination
	
@given("the gripstate is 'closed'")
def setClosed(the_robot):
	the_robot.gripperArm.close()
	
@when("the rotate feature is called")
def callRotate(the_robot):
	the_robot.gripperArm.rotate(1)
	
@then("the auto-orient function is called")
def autoOrientWasCalled(the_robot):
	assert the_robot.gripperArm._autoOriented == True

@then("the errorState is 'None'")
def errorStateIsNone(the_robot):
	assert the_robot.gripperArm.errorState == "None"
