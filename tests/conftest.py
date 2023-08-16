#conftest.py
import pandas as pd
import os
import pytest
from robot import robot
from athena import athena
from hera import hera
from hercules import hercules
from mercury import mercury
from perseus import perseus
from tests.testRobotRepository import testRobotRepository

from pytest_bdd import scenario, given, when, then, parsers

@pytest.fixture
def spec_sheet(request):
    dir, null = os.path.split(str(request.path))
    fileName = dir + "\\resources\\robots.xlsx"

    return pd.read_excel(io=fileName, sheet_name="data")

def pytest_bdd_before_scenario(request, feature, scenario):
    robot.repo = testRobotRepository()

def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    #print('whatever is going on')
    # log changes in state
    pass