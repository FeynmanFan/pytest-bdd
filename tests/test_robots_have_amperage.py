import pytest
from velocity import velocity
from robot import robot
from athena import athena
from hera import hera
from hercules import hercules
from mercury import mercury
from perseus import perseus

from pytest_bdd import scenario, given, when, then, parsers

@scenario("../features/robots_have_amperage.feature", "The robot has enough amperage to power all sensors")
def test_specs():
    pass

@pytest.fixture
def the_robot():
    pass

@given(parsers.parse("the robot is model {robotModel}"), target_fixture="the_robot")
def robotIsModel(robotModel):
    if robotModel == "athena":
        return athena()
    elif robotModel == "hercules":
        return hercules()
    elif robotModel == "hera":
        return hera()
    elif robotModel == "perseus":
        return perseus()
    elif robotModel == "mercury":
        return mercury()


@when("the robot performs an amperage check")
def performAmperageCheck(the_robot):
    the_robot.checkAmperage()

@then("the power state of the unit is ALL")
def powerStateIsALL(the_robot):
    assert the_robot.powerState == "ALL"