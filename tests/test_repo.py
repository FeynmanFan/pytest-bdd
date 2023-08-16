from tests.testRobotRepository import testRobotRepository
from robotRepository import robotRepository
from robot import robot
from athena import athena

def test_setRepo():
    repo = testRobotRepository()
    robot.repo = repo

    ath = athena()

    assert (ath.repo.title == "Test Repo")