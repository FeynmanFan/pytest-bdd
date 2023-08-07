import pytest
from pytest_bdd import scenarios, scenario, given, when, then
from robot import robot
from velocity import velocity

@pytest.fixture
def the_robot():
    return robot(velocity(0, 0))

@pytest.fixture
def theNearFieldSensor():
    nearFieldSensorValue = False
    return nearFieldSensorValue

@scenario("../features/slowdownwhenobjectnearby.feature", "Robot detects object while in motion")
def test_slowdown():
    return 

@given("the near field sensor detects an object", target_fixture="theNearFieldSensor")
@given("the robot is traveling at 10m/s")
def robot_travelling(theNearFieldSensor, the_robot):
    theNearFieldSensor = True
    the_robot.velocity.speed = 10
    
    return theNearFieldSensor
    
@when("motion evaluation fires")
def robotMotionFired(the_robot, theNearFieldSensor):
    print("in test: nearfieldDetected " + str(theNearFieldSensor))
    the_robot.motionEvaluation(theNearFieldSensor)

@then("speed should be 9m/s")
def robotSpeedSlower(the_robot):
    assert the_robot.velocity.speed == 9