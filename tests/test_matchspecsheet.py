import pytest
import os
import pandas as pd
from velocity import velocity
from robot import robot
from athena import athena
from hera import hera
from hercules import hercules
from mercury import mercury
from perseus import perseus

from pytest_bdd import scenario, given, when, then, parsers

@scenario("../features/matchspecsheet.feature", "Robots' load values in software match the spec sheet")
def test_specs():
    pass

@pytest.fixture
def the_robot():
    pass

@pytest.fixture
def the_loadWeight():
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
    
@given("the load meets the spec", target_fixture="the_loadWeight")
def loadWeight(the_robot, spec_sheet):
    for index, row in spec_sheet.iterrows():
        if row[0] == the_robot.model:
            print("loadweight: " + str(row[1]))
            return int(row[1])
        
    raise Exception("Could not find model '" + the_robot.model + "'")
    
@when("the robot is loaded")
def robotIsLoaded(the_robot, the_loadWeight):
    print(the_loadWeight)

    the_robot.load(the_loadWeight)

@then("the loadState is within the cargo capacity of the model")
def loadStateWithinTolerance(the_robot):
    assert the_robot.loadState == "NORMAL"