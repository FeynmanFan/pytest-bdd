import pytest
from pytest_bdd import scenario, given, when, then, parsers
from robot import robot
from velocity import velocity

#Background:
#	Given the near field sensor detects an object

@pytest.fixture
def the_robot():
	return robot(velocity(0,0))

@pytest.fixture
def theNearFieldSensor():
	nearFieldSensor = False
	return nearFieldSensor

@scenario("../features/slowdownwhenobjectnearby.feature", "Robot detects object while in motion")
def test_slowdown():
	return
	
@given("the near field sensor detects an object", target_fixture="theNearFieldSensor")
def sensor_fired(theNearFieldSensor):
	#print('nearfieldsensor' + '\t\t' + str(time.time()))
	theNearFieldSensor = True
	return theNearFieldSensor

@given(parsers.cfparse("the robot is traveling at {initialSpeed: d}m/s"))
def robot_travelling(the_robot, initialSpeed):
	#print('initialSpeed' + '\t\t' + str(time.time()))
	the_robot.velocity.speed = initialSpeed

@when("motion evaluation fires")
def robotMotionFired(theNearFieldSensor, the_robot):
	the_robot.motionEvaluation(theNearFieldSensor)

@then(parsers.cfparse("speed should be {finalSpeed: d}m/s"))
def robotSpeedSlower(the_robot, finalSpeed):
	assert(the_robot.velocity.speed == finalSpeed, "Robot slows down by 1m/s")